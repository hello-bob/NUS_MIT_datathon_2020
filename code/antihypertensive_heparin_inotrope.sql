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
    MAX(CASE WHEN (drugName ILIKE '%Heparin%' 
                   OR drughiclseqno in (39654, 9545, 2807, 33442, 8643, 33314, 2808, 2810))
                   THEN 1 ELSE 0 END) AS heparin_iv,
    MAX(CASE WHEN ((drugName ILIKE '%Phenylephrine%' OR drughiclseqno in (37028, 35517, 35587, 2087))
                   OR (drugName ILIKE '%Norepinephrine%' OR drughiclseqno in (37410, 36346, 2051))
                   OR (drugName ILIKE '%Dopamine%' OR drughiclseqno in (2060, 2059))
                   OR (drugName ILIKE '%Dobutamine%' OR drughiclseqno in (8777, 40))
                   OR (drugName ILIKE '%Vasopressin%' OR drughiclseqno in (38884, 38883, 2839)))
                   THEN 1
                   ELSE 0 END) AS inotropes
FROM medication
WHERE drugOrderCancelled = 'No' AND (drugStartOffset > 0 AND drugStartOffset < 6*60)
GROUP BY patientunitstayid)

SELECT * FROM medication_agg_drug