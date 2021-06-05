CREATE TABLE eicu_top_5_meds AS (
WITH medication_agg_drug AS (SELECT patientunitstayid,
    MAX(CASE WHEN (drugName ILIKE '%nitroprusside%'
                   OR drugName ILIKE '%Hydralazine%'
                   OR drugName ILIKE '%Nicardipine%'
                   OR drugName ILIKE '%labetalol%'
                   OR drugName ILIKE '%esmolol%')
                   THEN 1
                   ELSE 0 END) AS medication_top_5
                            FROM medication
                            WHERE drugOrderCancelled = 'No'AND drugStartOffset < 6*60
                            GROUP BY patientunitstayid),
                            
treatment_agg_drug AS (SELECT patientunitstayid,
MAX(CASE WHEN (treatmentString ILIKE '%nitroprusside%'
    OR treatmentString ILIKE '%Hydralazine%'
    OR treatmentString ILIKE '%Nicardipine%'
    OR treatmentString ILIKE '%labetalol%'
    OR treatmentString ILIKE '%esmolol%')
THEN 1
ELSE 0 END) AS treatment_top_5
FROM treatment
WHERE treatmentOffset < 6*60
GROUP BY patientunitstayid)

SELECT patientunitstayid, CASE WHEN (medication_top_5+treatment_top_5 >0) THEN 1 ELSE 0 END AS top_5_drugs
FROM medication_agg_drug JOIN treatment_agg_drug USING (patientunitstayid)
)