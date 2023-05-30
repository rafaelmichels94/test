Projeto: Backend IA/Images
- Esse backend sera responsavel por todo o gerenciamento das imagens: salvar, manipular, colocar em uma fila pra ser julgado pela IA, disponibilizar para futura analise.

- [x] Estrutura base do backend 2h
- [x] Definir modelo das imagens: Campos pra serem criados no database 1h
- [em progresso] Endpoint Images: Get/Post(Upload)/Get List(Pra usar no treinamento) 6h
  - [ ] Definir assinatura de request/response com o Marco/app 1h
- [ ] Painel de admin para images: Maneira de gerenciar as imagens 4h
- [ ] Definir estrutura das filas: Celery, Celery Beat, Flower 2h
- [ ] Implementar a estrutura de filas: Containers, Tarefas periodicas, Fallback 6h
- [ ] Criar pagina que liste as imagens estilo tinder para treinamento 4h
- [ ] Estudar estrategias de pre-processamento de imagens 5h
- [ ] Estudar formas de fazer o reconhecimento de imagens ex: Haar Cascade 5h
- [ ] Implementar modelo de reconhecimento 10h
- [ ] Testar o modelo, usar outras imagens e validar as respostas com especialistas 4h
- [ ] Validar a velocidade de responsta do modelo 30min
- [ ] Criar task pra rodar o modelo na imagens do database 4h

- Bloqueado: precisa das imagens finais usando o dispositivo otico final
  - [ ] Receber imagens
  - [ ] Ter o auxilio de especialistas para julgar as imagens
  - [ ] Com as imagens definidas treinar a IA para a classificacao da larva

- Bloqueado: precisa da infra
  - [ ] Definir pipelines de deploy/tests
  - [ ] Fazer golive no servidor de producao


