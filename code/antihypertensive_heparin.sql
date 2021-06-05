WITH medication_agg_drug AS (

SELECT patientunitstayid,
    MAX(CASE WHEN (drugName ILIKE '%nitroprusside%'
                   OR drugName ILIKE '%Hydralazine%'
                   OR drugName ILIKE '%Nicardipine%'
                   OR drugName ILIKE '%labetalol%'
                   OR drugName ILIKE '%esmolol%')
                   THEN 1
                   ELSE 0 END) AS antihypertensive_iv_tight_control,
    MAX(CASE WHEN (drugName ILIKE '%atenolol%'
                   OR drugName ILIKE '%metoprolol%'
                   OR drugName ILIKE '%Dilitazem%'
                   OR drugName ILIKE '%Verapamil%'
                   OR drugName ILIKE '%furosemide%')
                   THEN 1
                   ELSE 0 END) AS antihypertensive_iv_non_tight_control,
    MAX(CASE WHEN drugName ILIKE '%Heparin%' THEN 1 ELSE 0 END) AS heparin_iv,
    MAX(CASE WHEN (drugName ILIKE '%Phenylephrine%'
                   OR drugName ILIKE '%Norepinephrine%'
                   OR drugName ILIKE '%Dopamine%'
                   OR drugName ILIKE '%Dobutamine%'
                   OR drugName ILIKE '%Vasopressin%')
                   THEN 1
                   ELSE 0 END) AS inotropes
FROM medication
WHERE drugOrderCancelled = 'No' AND (drugStartOffset > 0 AND drugStartOffset < 6*60)
GROUP BY patientunitstayid)

SELECT * FROM medication_agg_drug