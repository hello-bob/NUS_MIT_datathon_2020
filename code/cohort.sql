create table cohort as (
with cohort as (
select distinct admissions.* from diagnoses_icd
join admissions
using (hadm_id)
where icd_code in ('43301', '43311', '43321', '43331', '43381', '43391')
or icd_code ilike '434%'
),
tpa as (
select * from inputevents
where itemid = 221319
),
dapt as (
SELECT * from prescriptions
where drug ilike '%clopidogrel%'
or drug ilike '%ticagrelor%'
or drug ilike '%prasugrel%'
or drug ilike '%aspirin%'
)
select *
from cohort
where hadm_id not in (select distinct hadm_id from tpa)
and hadm_id not in (SELECT DISTINCT hadm_id from dapt)
)