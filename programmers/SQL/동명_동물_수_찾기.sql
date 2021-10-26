    SELECT NAME, COUNT(ANIMAL_ID)
      FROM ANIMAL_INS
     WHERE NAME IS NOT NULL
  GROUP BY NAME
    HAVING COUNT(NAME) >= 2
  ORDER BY NAME