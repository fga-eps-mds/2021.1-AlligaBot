#!/usr/bin/python3

import os
import glob
from datetime import date, timedelta
import shutil


markdown_files = glob.glob('*.md')
markdown_files_in_order = [
  'Termo-de-Abertura-do-Projeto.md',
  'documento-de-arquitetura.md',
  'documento-de-visao.md',
  'Requisitos do produto.md',
  'IdentidadeVisual.md',
  'PersonalidadeDoBot.md',
  'documento-de-estrutura-analitica.md',
  'plano-de-gerenciamento-de-riscos.md',
  'plano-de-comunicacao.md',
  'documento-de-prototipo.md',
  'canvas.md',
  'documento-de-backlog.md',
  'roadmap.md', # roadmap de produto?
  'documento-de-devops.md',
  'CONTRIBUTING.md',
  'template.md',
  'commits.md',
  'branches.md',
  'folha-de-estilo.md',
  'CODE_OF_CONDUCT.md',
  # 'about.md',
]

initial_date = date(2021, 8, 1)
days_period = timedelta(days=1)

for i, filename in enumerate(markdown_files_in_order):

  file = open(filename, 'r')
  file_content = file.read()
  file.close()
  file = open(f'_posts/{filename}', 'w')
  file.write('---\nexcerpt: ""\n---\n')
  file.write(file_content)
  file.close()

  initial_date += days_period
  os.rename(f'_posts/{filename}', f'_posts/{initial_date}-{filename.lower()}')

# print(markdown_files)