CREATE OR REPLACE PROCEDURE locs_num()
AS $$
DECLARE
  cursor_flm CURSOR FOR
  SELECT nome, cod_filme FROM filme;
  nome_flm VARCHAR;
  cod_flm  INTEGER;
  cod_exp  INTEGER;
  num_locs INTEGER;
BEGIN
  OPEN cursor_flm;
  RAISE INFO 'FILME - TOTAL DE LOCACOES';
  LOOP
    FETCH NEXT FROM cursor_flm INTO nome_flm, cod_flm;
    IF NOT FOUND THEN EXIT;
    END IF;

    IF num_locs = 0 THEN RAISE INFO '% - NAO TEVE LOCACOES', nome_flm;

    ELSE
      SELECT cod_exemplar INTO cod_exp
      FROM exemplar e
      WHERE cod_flm = e.cod_filme;

      SELECT COUNT(*) INTO num_locs
      FROM locacao l
      WHERE cod_exp = l.cod_exemplar;

      RAISE INFO '% - %', nome_flm, num_locs;
    END IF;
  END LOOP;
END;
$$ LANGUAGE plpgsql;

CALL locs_num();