# the following query re-queues orgs with missing relationships 
# (i.e. where one side of the relationship has a REL credential and the other doesn't)

insert into event_by_corp_filing
(system_type_cd, corp_num, prev_event_id, prev_event_date, last_event_id, last_event_date, entry_date)
select 'BC_REG', missing_corp_num, 0, '0001-01-01 00:00:00', event_id, event_date, now()
from (select 
  foo.corp_num as corp_num_1, foo.registration_id as registration_id, 
  foo.associated_registration_id as associated_registration_id,
  (CASE WHEN foo.associated_registration_id ilike 'BC%' 
   THEN substring(foo.associated_registration_id, 3)
   ELSE foo.associated_registration_id END) AS missing_corp_num,
  c_log.corp_num as corp_num_2, c_log.credential_json->>'registration_id', 
  c_log.credential_json->>'associated_registration_id'
from 
(select * from credential_log
where credential_type_cd = 'REL') as c_log
right join
(select corp_num, 
   credential_json->>'registration_id' as registration_id, 
   credential_json->>'associated_registration_id' as associated_registration_id
from credential_log
where credential_type_cd = 'REL') as foo
on c_log.credential_json->>'registration_id' = foo.associated_registration_id
and c_log.credential_json->>'associated_registration_id' = foo.registration_id
where c_log.corp_num is null or foo.corp_num is null
  and c_log.corp_num not in
  (select corp_num from corp_history_log where process_msg = 'Withdrawn')) as MISSING_CORP_RELN, 
  LAST_EVENT
where LAST_EVENT.record_id = (select max(record_id) from LAST_EVENT);
