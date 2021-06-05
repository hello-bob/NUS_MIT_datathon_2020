with raw_bp as (
select cohort.hadm_id, cohort.admittime, vitalsign.*, (charttime - admittime) as bp_time from cohort
join icustays 
on cohort.hadm_id = icustays.hadm_id
join vitalsign
on icustays.stay_id = vitalsign.stay_id
where (charttime - admittime) < interval '6' hour
)
select subject_id, hadm_id,
min(mbp) as min_mbp,
max(mbp) as max_mbp,
avg(mbp) as avg_mbp,
min(mbp_ni) as min_mbp_ni,
max(mbp_ni) as max_mbp_ni,
avg(mbp_ni) as avg_mbp_ni
from raw_bp
group by 1,2