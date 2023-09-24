--local save of the VIEW exercice

-- Exercicio 1
-- Visão com nome dos filmes lançados apos 2000, asc.

DROP VIEW pos2000;

CREATE VIEW pos2000 AS
SELECT f.nome
FROM filme f
WHERE ano < 2000
ORDER BY ano;

SELECT * FROM pos2000;


-- Exercicio 2
-- Visão com nome dos filmes lançados antes 2000, asc, com Kenneth

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
CREATE OR 