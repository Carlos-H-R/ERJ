-- Exercicio 1

DROP VIEW pos2000;

CREATE VIEW pos2000 AS
SELECT f.nome
FROM filme f
WHERE ano < 2000
ORDER BY ano;

SELECT * FROM pos2000;


-- Exercicio 2

DROP VIEW ken_bra_a2000;

CREATE VIEW ken_bra_a2000 AS
SELECT f.nome
FROM filme f, participacao pt, profissional_cinema pc
WHERE ano < 2000 AND
      f.cod_filme = pt.cod_filme AND
      pc.nome = 'Kenneth Branagh'
GROUP BY f.nome
ORDER BY f.nome;

SELECT * FROM ken_bra_a2000;


-- Exercicio 3
DROP VIEW ken_bra_princ;

CREATE VIEW ken_bra_princ AS
SELECT f.nome
FROM filme f, participacao pt, profissional_cinema pc
WHERE ano < 2000 AND
      f.cod_filme = pt.cod_filme AND
      pc.nome = 'Kenneth Branagh' AND
      pt.cod_papel = 1
GROUP BY f.nome      
ORDER BY f.nome;

SELECT * FROM ken_bra_princ;


-- Exercicio 4
CREATE VIEW all_papers AS
SELECT nome
FROM participacao part, profissional_cinema prof
WHERE prof.cod_profissional_cinema = part.cod_profissional_cinema
GROUP BY nome
HAVING COUNT(DISTINCT cod_papel) > 3;

SELECT * FROM all_papers;

