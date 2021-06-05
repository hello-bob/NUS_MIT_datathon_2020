with cohort as (
select distinct admissions.* from diagnoses_icd
join admissions
using (hadm_id)
where icd_code in ('43301', '43311', '43321', '43331', '43381', '43391')
or icd_code ilike '434%'
or icd_code ilike 'I62%'
or icd_code ilike 'I63%'
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
),
tmb as (
select * from procedures_icd join
d_icd_procedures using (icd_code)
where icd_code = '3974'
)
select *
from cohort
where hadm_id not in (select distinct hadm_id from tpa)
and hadm_id not in (SELECT DISTINCT hadm_id from dapt)
and hadm_id not in (SELECT DISTINCT hadm_id from tmb)

