-- Exercício 1

CREATE OR REPLACE FUNCTION join_txt(text1 varchar(30), text2 varchar(30))
RETURNS varchar(60) AS $$
DECLARE
  txt varchar(60);
BEGIN
  txt := text1 || text2;
  RETURN txt;
END;
$$ LANGUAGE plpgsql;

SELECT SaveText('Olá.','Tudo Bem?');


-- Exercício 2

CREATE OR REPLACE FUNCTION origin_movie(cod integer)
RETURNS TABLE(pt varchar(100), en varchar(100)) AS 
$$
BEGIN
  RETURN QUERY 
  SELECT nome, nome_original 
  FROM filme
  WHERE cod = cod_filme;
END;
$$ LANGUAGE plpgsql;


select origin_movie(15);


-- Exercício 3

CREATE OR REPLACE FUNCTION odd_even(valor int)
RETURNS varchar(10) AS
$$
DECLARE
  result varchar(10);
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

CREATE OR REPLACE FUNCTION fact(valor int)
RETURNS integer AS
$$
DECLARE 
  n integer;
  p integer;
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

CREATE OR REPLACE FUNCTION check_disp(a integer, cens integer)
RETURNS TABLE(disp bigint) AS
$$
BEGIN
  RETURN QUERY SELECT COUNT(*) FROM filme f
  WHERE f.ano = a AND
        f.censura = cens;
END;
$$ LANGUAGE plpgsql;


SELECT check_disp(1999,18);