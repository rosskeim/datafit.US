SELECT 
	COUNT(CASE bpart WHEN 'quad' THEN 1 ELSE NULL END) 'quad', 
	COUNT(CASE bpart WHEN 'ham' THEN 1 ELSE NULL END) 'ham',
	COUNT(CASE bpart WHEN 'calf' THEN 1 ELSE NULL END) 'calf',
	COUNT(CASE bpart WHEN 'back' THEN 1 ELSE NULL END) 'back',
	COUNT(CASE bpart WHEN 'bicep' THEN 1 ELSE NULL END) 'bicep',
	COUNT(CASE bpart WHEN 'fdelt' THEN 1 ELSE NULL END) 'fdelt',
	COUNT(CASE bpart WHEN 'rsdelt' THEN 1 ELSE NULL END) 'rsdelt',
	COUNT(CASE bpart WHEN 'tricep' THEN 1 ELSE NULL END) 'tricep',
	COUNT(CASE bpart WHEN 'chest' THEN 1 ELSE NULL END) 'chest'
FROM training_log
