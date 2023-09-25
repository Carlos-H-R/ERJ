-- Exercício 1

CREATE OR REPLACE FUNCTION join_txt(text1 VARCHAR(30), text2 VARCHAR(30))
RETURNS VARCHAR(60) AS $$
DECLARE
  txt VARCHAR(60);
BEGIN
  txt := text1 || text2;
  RETURN txt;
END;
$$ LANGUAGE plpgsql;

SELECT SaveText('Olá.','Tudo Bem?');



-- Exercício 2

CREATE OR REPLACE FUNCTION origin_movie(cod INTEGER)
RETURNS TABLE(pt VARCHAR(100), en VARCHAR(100)) AS 
$$
BEGIN
  RETURN QUERY 
  SELECT nome, nome_original 
  FROM filme
  WHERE cod = cod_filme;
END;
$$ LANGUAGE plpgsql;


SELECT origin_movie(15);



-- Exercício 3

CREATE OR REPLACE FUNCTION odd_even(valor INTEGER)
RETURNS VARCHAR(10) AS
$$
DECLARE
  result VARCHAR(10);
BEGIN
  IF (valor % 2) = 0 
  THEN result := 'Eh par!';
  ELSE result := 'Eh ímpar!';
  END IF;
  
  RETURN result;
END;
$$ LANGUAGE plpgsql;


SELECT odd_even(16);



-- Exercício 4

CREATE OR REPLACE FUNCTION fact(valor INTEGER)
RETURNS INTEGER AS
$$
DECLARE 
  n INTEGER;
  p INTEGER;
BEGIN
  n := valor;
  p := n - 1;

  WHILE p > 0
  LOOP 
    n := n * p;
    p := p - 1;
  END LOOP;
END;
$$ plpgsql;

SELECT fact(4);



-- Exercício 5

CREATE OR REPLACE FUNCTION check_disp(a INTEGER, cens INTEGER)
RETURNS TABLE(disp BIGINT) AS
$$
BEGIN
  RETURN QUERY SELECT COUNT(*) FROM filme f
  WHERE f.ano = a AND
        f.censura = cens;
END;
$$ LANGUAGE plpgsql;


SELECT check_disp(1999,18);