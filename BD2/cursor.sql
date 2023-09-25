-- Exercício 1

CREATE OR REPLACE FUNCTION class_cens()
RETURNS TABLE(nome_f VARCHAR, str_class VARCHAR) AS 
$$
DECLARE
  cursor_class CURSOR FOR
  SELECT nome, censura FROM filme;
  num_class INTEGER;
  nome_f VARCHAR;
  str_class VARCHAR;
BEGIN 
  OPEN cursor_class;
  LOOP
    FETCH NEXT FROM cursor_class INTO nome_f, num_class;
    EXIT WHEN NOT FOUND;

    IF (num_class < 16) THEN str_class := 'Infantil';
    ELSIF (num_class >= 16 AND num_class < 18) THEN str_class := 'Adolescente';
    ELSIF (num_class >= 18) THEN str_class := 'Adulto';
    END IF;

    RETURN QUERY VALUES (nome_f,str_class);
  END LOOP;
  CLOSE cursor_class;
END;
$$ LANGUAGE plpgsql;


SELECT class_cens();



-- Exercício 2

CREATE OR REPLACE FUNCTION double_value(nome_f VARCHAR)
RETURNS NUMERIC AS
$$
DECLARE
  cursor_price CURSOR FOR
  SELECT preco_sugerido_locacao FROM filme
  WHERE filme.nome = nome_f;
  rec_price NUMERIC;
  final_price NUMERIC;
BEGIN
    OPEN cursor_price;
    FETCH FROM cursor_price INTO rec_price;

    final_price := 2 * rec_price;
    RETURN final_price;
    CLOSE cursor_price;
END;
$$ LANGUAGE plpgsql;

select double_value('Advogado do Diabo')