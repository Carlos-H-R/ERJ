data Status = Status String String Int (Int, Int, Int, Int)
-- Nome,  Raca, idade,  Status(Forca, defesa, agilidade, HP)

data Personagem = Guerreiro Status String Int | Mago Status Int [(String, String)] | Sacerdote Status Int (String, String) Int

-- Guerreiro -> Destreza com algum tipo de armas / Duracao Rage mode
-- Mago -> maximo Magic Power - MP / Lista de Feiticos e seu efeito 
-- sacerdote -> Poder de cura por ativacao / Lista de aprimoramentos / tempo da oracao

kiron = Mago (Status "Kiron" "Humano" 28 (11, 16, 9, 17)) 12 [("Fire Bolt", "1d6 de dano de fogo"), ("Shield", "quando atacado consome uma ação e aluna o dano")]