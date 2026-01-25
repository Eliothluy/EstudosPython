"""
🎯 PLANO DE ESTUDOS GAMIFICADO: Python + Data Science + OPEN RAN
Versão 2.0 - Com NS3, Estatística e Gamificação
"""

import json
import datetime
import time
import random
import os
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum
import pandas as pd
import numpy as np
from collections import defaultdict

class Status(Enum):
    NAO_INICIADO = "🔴 Não Iniciado"
    EM_ANDAMENTO = "🟡 Em Andamento"
    CONCLUIDO = "✅ Concluído"

class NivelDificuldade(Enum):
    FACIL = "🟢 Fácil"
    MEDIO = "🟡 Médio"
    DIFICIL = "🔴 Difícil"
    EXPERT = "🟣 Expert"

@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str
    nivel: NivelDificuldade
    status: Status
    data_inicio: Optional[str]
    data_conclusao: Optional[str]
    duracao_estimada: int  # em horas
    xp_recompensa: int
    dependencias: List[int]
    tags: List[str]

@dataclass
class Modulo:
    id: int
    titulo: str
    descricao: str
    tarefas: List[Tarefa]
    objetivo: str
    xp_modulo: int

class PlanoEstudosGamificado:
    def __init__(self, usuario: str = "Estudante"):
        self.usuario = usuario
        self.nivel = 1
        self.xp_total = 0
        self.xp_necessario_proximo_nivel = 100
        self.streak = 0  # dias consecutivos estudando
        self.ultimo_acesso = None
        self.modulos = []
        self.conquistas = []
        self._carregar_plano_completo()
        self._carregar_progresso()
        
    def _carregar_plano_completo(self):
        """Carrega o plano de estudos completo com todos os módulos"""
        
        # MÓDULO 1: Fundamentos Python & Estatística
        modulo1 = Modulo(
            id=1,
            titulo="📚 Mês 1: Python & Estatística Básica",
            descricao="Fundamentos de Python e conceitos estatísticos essenciais",
            tarefas=[
                Tarefa(101, "Variáveis e Tipos de Dados", 
                      "Exercícios com tipos básicos e operações matemáticas", 
                      NivelDificuldade.FACIL, Status.NAO_INICIADO, None, None, 2, 10, [], ["python", "basico"]),
                Tarefa(102, "Estruturas de Controle", 
                      "If/else, loops for/while com exemplos telecom", 
                      NivelDificuldade.FACIL, Status.NAO_INICIADO, None, None, 3, 15, [101], ["python", "telecom"]),
                Tarefa(103, "Estatística Descritiva I", 
                      "Média, mediana, moda, variância, desvio padrão", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 4, 20, [], ["estatistica", "matematica"]),
                Tarefa(104, "Listas e Dicionários", 
                      "Manipulação de estruturas de dados com dados de rede", 
                      NivelDificuldade.FACIL, Status.NAO_INICIADO, None, None, 3, 15, [101], ["python", "dados"]),
                Tarefa(105, "Funções e Módulos", 
                      "Criar funções reutilizáveis para cálculos telecom", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 4, 20, [102, 104], ["python", "funcoes"]),
                Tarefa(106, "Probabilidade Básica", 
                      "Conceitos de probabilidade, distribuições simples", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 5, 25, [103], ["probabilidade", "matematica"]),
                Tarefa(107, "Projeto 1: Simulador de Métricas", 
                      "Gerador de KPIs de rede com análise estatística", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 6, 30, [105, 106], ["projeto", "telecom", "python"]),
            ],
            objetivo="Domínio dos fundamentos de Python e estatística descritiva",
            xp_modulo=150
        )
        
        # MÓDULO 2: Data Science Essencial
        modulo2 = Modulo(
            id=2,
            titulo="📊 Mês 2: Data Science & Visualização",
            descricao="Pandas, visualização e estatística inferencial",
            tarefas=[
                Tarefa(201, "Pandas Básico", 
                      "DataFrames, séries, operações com dados telecom", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 5, 25, [107], ["pandas", "datascience"]),
                Tarefa(202, "Visualização com Matplotlib", 
                      "Gráficos de KPIs, séries temporais de rede", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 4, 20, [201], ["visualizacao", "matplotlib"]),
                Tarefa(203, "Estatística Inferencial", 
                      "Testes de hipótese, intervalo de confiança", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 6, 30, [106], ["estatistica", "inferencial"]),
                Tarefa(204, "Seaborn e Plotly", 
                      "Visualizações avançadas para dashboards", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 5, 25, [202], ["visualizacao", "dashboard"]),
                Tarefa(205, "Correlação e Regressão", 
                      "Análise de correlação entre métricas de rede", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 6, 30, [203], ["estatistica", "regressao"]),
                Tarefa(206, "Projeto 2: Dashboard de KPIs", 
                      "Dashboard interativo para monitoramento de rede", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 8, 40, [204, 205], ["projeto", "dashboard", "telecom"]),
            ],
            objetivo="Criação de dashboards e análises estatísticas avançadas",
            xp_modulo=200
        )
        
        # MÓDULO 3: Machine Learning Telecom
        modulo3 = Modulo(
            id=3,
            titulo="🤖 Mês 3: Machine Learning Aplicado",
            descricao="Algoritmos de ML para otimização de redes",
            tarefas=[
                Tarefa(301, "Regressão para Previsão", 
                      "Prever throughput baseado em métricas", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 6, 30, [206], ["ml", "regressao"]),
                Tarefa(302, "Classificação de Falhas", 
                      "Identificar células problemáticas com ML", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 7, 35, [301], ["ml", "classificacao"]),
                Tarefa(303, "Clustering de Células", 
                      "Agrupar células por padrão de comportamento", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 6, 30, [301], ["ml", "clustering"]),
                Tarefa(304, "Séries Temporais Telecom", 
                      "Previsão de carga usando ARIMA/Prophet", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 8, 40, [301], ["series-temporais", "previsao"]),
                Tarefa(305, "Detecção de Anomalias", 
                      "Identificar comportamentos anormais na rede", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 7, 35, [302, 303], ["ml", "anomalias"]),
                Tarefa(306, "Projeto 3: Sistema de Alerta Inteligente", 
                      "Sistema ML completo para monitoramento proativo", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 10, 50, [304, 305], ["projeto", "ml", "telecom"]),
            ],
            objetivo="Implementação de modelos de ML para otimização de rede",
            xp_modulo=250
        )
        
        # MÓDULO 4: OPEN RAN & NS3
        modulo4 = Modulo(
            id=4,
            titulo="📡 Mês 4: OPEN RAN & Simulação NS3",
            descricao="Arquitetura OPEN RAN e simulações com NS3",
            tarefas=[
                Tarefa(401, "Arquitetura OPEN RAN", 
                      "Componentes O-RAN, RIC, xApps, interfaces", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 5, 25, [206], ["openran", "arquitetura"]),
                Tarefa(402, "Introdução ao NS3", 
                      "Instalação, primeiros scripts, conceitos básicos", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 6, 30, [], ["ns3", "simulacao"]),
                Tarefa(403, "Simulações 5G no NS3", 
                      "Configuração de cenários 5G, coleta de métricas", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 8, 40, [402], ["ns3", "5g", "simulacao"]),
                Tarefa(404, "Probabilidade Aplicada a Redes", 
                      "Teoria das filas, processos estocásticos em redes", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 7, 35, [106], ["probabilidade", "redes", "matematica"]),
                Tarefa(405, "Modelos de Tráfego no NS3", 
                      "Implementar diferentes modelos de tráfego", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 8, 40, [403], ["ns3", "trafego", "modelos"]),
                Tarefa(406, "Projeto 4: Simulador OPEN RAN", 
                      "Simulação completa de cenário OPEN RAN com NS3", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 12, 60, [401, 405], ["projeto", "ns3", "openran"]),
            ],
            objetivo="Simulação de cenários OPEN RAN usando NS3",
            xp_modulo=250
        )
        
        # MÓDULO 5: xApps & Implantação
        modulo5 = Modulo(
            id=5,
            titulo="🚀 Mês 5: xApps & Implantação",
            descricao="Desenvolvimento de xApps e deploy em produção",
            tarefas=[
                Tarefa(501, "Desenvolvimento de xApps", 
                      "Estrutura de xApp, integração com RIC", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 7, 35, [406], ["xapp", "openran", "desenvolvimento"]),
                Tarefa(502, "APIs REST para Telecom", 
                      "API Gateway, autenticação, documentação OpenAPI", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 6, 30, [501], ["api", "rest", "telecom"]),
                Tarefa(503, "Integração ML no xApp", 
                      "Embedding de modelos, inferência em tempo real", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 8, 40, [306, 501], ["ml", "xapp", "integracao"]),
                Tarefa(504, "Docker e Kubernetes", 
                      "Containerização, orquestração, helm charts", 
                      NivelDificuldade.DIFICIL, Status.NAO_INICIADO, None, None, 7, 35, [502], ["docker", "kubernetes", "devops"]),
                Tarefa(505, "Testes e CI/CD", 
                      "Testes unitários, integração, pipelines GitHub Actions", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 8, 40, [504], ["testes", "ci-cd", "devops"]),
                Tarefa(506, "Projeto Final: xApp Completo", 
                      "xApp de otimização com ML, deploy em K8s", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 15, 75, [503, 505], ["projeto-final", "xapp", "openran"]),
            ],
            objetivo="Desenvolvimento e deploy de xApp completo em produção",
            xp_modulo=300
        )
        
        # MÓDULO 6: Projeto Final & Estatística Avançada
        modulo6 = Modulo(
            id=6,
            titulo="🏆 Mês 6: Projeto Final & Avançado",
            descricao="Projeto integrado e tópicos avançados",
            tarefas=[
                Tarefa(601, "Otimização Estocástica", 
                      "Algoritmos genéticos, simulated annealing para redes", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 10, 50, [404], ["otimizacao", "estocastico", "matematica"]),
                Tarefa(602, "Análise de Séries Temporais Avançada", 
                      "Modelos state-space, deep learning para séries temporais", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 10, 50, [304], ["series-temporais", "deep-learning"]),
                Tarefa(603, "Simulação NS3 Avançada", 
                      "Customização de protocolos, análise de performance", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 12, 60, [406], ["ns3", "avancado", "simulacao"]),
                Tarefa(604, "Documentação e Apresentação", 
                      "Documentar projeto, criar apresentação técnica", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 8, 40, [506], ["documentacao", "apresentacao"]),
                Tarefa(605, "Preparação para Entrevistas", 
                      "Cases técnicos, perguntas comuns, portfolio", 
                      NivelDificuldade.MEDIO, Status.NAO_INICIADO, None, None, 6, 30, [604], ["carreira", "entrevistas"]),
                Tarefa(606, "Certificação Final", 
                      "Prova final, projeto revisado, certificado", 
                      NivelDificuldade.EXPERT, Status.NAO_INICIADO, None, None, 10, 100, [601, 602, 603, 604, 605], ["certificacao", "final"]),
            ],
            objetivo="Conclusão do projeto final e preparação profissional",
            xp_modulo=400
        )
        
        self.modulos = [modulo1, modulo2, modulo3, modulo4, modulo5, modulo6]
        
    def _carregar_progresso(self):
        """Carrega o progresso salvo do usuário"""
        try:
            with open(f'progresso_{self.usuario}.json', 'r') as f:
                data = json.load(f)
                self.nivel = data.get('nivel', 1)
                self.xp_total = data.get('xp_total', 0)
                self.xp_necessario_proximo_nivel = data.get('xp_necessario_proximo_nivel', 100)
                self.streak = data.get('streak', 0)
                self.ultimo_acesso = data.get('ultimo_acesso')
                self.conquistas = data.get('conquistas', [])
                
                # Atualizar status das tarefas
                for modulo in self.modulos:
                    for tarefa in modulo.tarefas:
                        tarefa_id = str(tarefa.id)
                        if tarefa_id in data.get('tarefas_concluidas', {}):
                            tarefa_data = data['tarefas_concluidas'][tarefa_id]
                            tarefa.status = Status.CONCLUIDO
                            tarefa.data_inicio = tarefa_data.get('data_inicio')
                            tarefa.data_conclusao = tarefa_data.get('data_conclusao')
        except FileNotFoundError:
            self._salvar_progresso()
            
    def _salvar_progresso(self):
        """Salva o progresso do usuário"""
        tarefas_concluidas = {}
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.status == Status.CONCLUIDO:
                    tarefas_concluidas[str(tarefa.id)] = {
                        'data_inicio': tarefa.data_inicio,
                        'data_conclusao': tarefa.data_conclusao
                    }
                    
        data = {
            'usuario': self.usuario,
            'nivel': self.nivel,
            'xp_total': self.xp_total,
            'xp_necessario_proximo_nivel': self.xp_necessario_proximo_nivel,
            'streak': self.streak,
            'ultimo_acesso': datetime.datetime.now().isoformat(),
            'conquistas': self.conquistas,
            'tarefas_concluidas': tarefas_concluidas
        }
        
        with open(f'progresso_{self.usuario}.json', 'w') as f:
            json.dump(data, f, indent=2)
            
    def _atualizar_streak(self):
        """Atualiza a streak de dias consecutivos"""
        hoje = datetime.datetime.now().date()
        
        if self.ultimo_acesso:
            ultimo = datetime.datetime.fromisoformat(self.ultimo_acesso).date()
            if (hoje - ultimo).days == 1:
                self.streak += 1
            elif (hoje - ultimo).days > 1:
                self.streak = 1
        else:
            self.streak = 1
            
        self.ultimo_acesso = hoje.isoformat()
        
    def completar_tarefa(self, tarefa_id: int):
        """Marca uma tarefa como concluída"""
        tarefa_encontrada = None
        modulo_encontrado = None
        
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.id == tarefa_id:
                    tarefa_encontrada = tarefa
                    modulo_encontrado = modulo
                    break
            if tarefa_encontrada:
                break
                
        if not tarefa_encontrada:
            print(f"❌ Tarefa {tarefa_id} não encontrada!")
            return
            
        # Verificar dependências
        for dep_id in tarefa_encontrada.dependencias:
            if not self._tarefa_concluida(dep_id):
                print(f"❌ Complete primeiro a tarefa {dep_id}!")
                return
                
        # Verificar se já está concluída
        if tarefa_encontrada.status == Status.CONCLUIDO:
            print(f"✅ Tarefa já estava concluída!")
            return
            
        # Marcar como concluída
        tarefa_encontrada.status = Status.CONCLUIDO
        tarefa_encontrada.data_conclusao = datetime.datetime.now().isoformat()
        
        # Adicionar XP
        self.xp_total += tarefa_encontrada.xp_recompensa
        print(f"🎉 +{tarefa_encontrada.xp_recompensa} XP ganhos!")
        
        # Verificar level up
        if self.xp_total >= self.xp_necessario_proximo_nivel:
            self.nivel += 1
            xp_excedente = self.xp_total - self.xp_necessario_proximo_nivel
            self.xp_necessario_proximo_nivel = int(self.xp_necessario_proximo_nivel * 1.5)
            self.xp_total = xp_excedente
            print(f"⭐ LEVEL UP! Agora você é nível {self.nivel}!")
            
            # Conquista por nível
            if self.nivel in [5, 10, 15, 20]:
                conquista = f"Nível {self.nivel}"
                if conquista not in self.conquistas:
                    self.conquistas.append(conquista)
                    print(f"🏆 Nova conquista: {conquista}!")
                    
        # Verificar se módulo foi completado
        modulo_completo = all(t.status == Status.CONCLUIDO for t in modulo_encontrado.tarefas)
        if modulo_completo:
            self.xp_total += modulo_encontrado.xp_modulo
            print(f"🏁 MÓDULO COMPLETO! +{modulo_encontrado.xp_modulo} XP!")
            
        self._atualizar_streak()
        self._salvar_progresso()
        print(f"✅ Tarefa '{tarefa_encontrada.titulo}' concluída com sucesso!")
        
    def _tarefa_concluida(self, tarefa_id: int) -> bool:
        """Verifica se uma tarefa está concluída"""
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.id == tarefa_id:
                    return tarefa.status == Status.CONCLUIDO
        return False
        
    def exibir_dashboard(self):
        """Exibe o dashboard principal do plano"""
        print("\n" + "="*60)
        print(f"🎮 PLANO DE ESTUDOS GAMIFICADO - {self.usuario}")
        print("="*60)
        
        # Barra de progresso do nível
        progresso = (self.xp_total / self.xp_necessario_proximo_nivel) * 100
        barra = "█" * int(progresso/5) + "░" * (20 - int(progresso/5))
        
        print(f"\n📊 SEU PROGRESSO:")
        print(f"   Nível: {self.nivel}  |  XP: {self.xp_total}/{self.xp_necessario_proximo_nivel}")
        print(f"   Progresso: [{barra}] {progresso:.1f}%")
        print(f"   Streak: {self.streak} dias consecutivos 🔥")
        print(f"   Tarefas concluídas: {self._contar_tarefas_concluidas()}/{self._contar_total_tarefas()}")
        print(f"   Módulos completos: {self._contar_modulos_concluidos()}/{len(self.modulos)}")
        
        # Próximas tarefas recomendadas
        print(f"\n🎯 PRÓXIMAS TAREFAS RECOMENDADAS:")
        recomendadas = self._obter_tarefas_recomendadas()
        for i, (modulo_id, tarefa) in enumerate(recomendadas[:3], 1):
            print(f"   {i}. [{modulo_id}.{tarefa.id}] {tarefa.titulo} ({tarefa.nivel.value})")
            
        # Conquistas
        if self.conquistas:
            print(f"\n🏆 CONQUISTAS OBTIDAS:")
            for conquista in self.conquistas[-3:]:  # Mostrar as 3 últimas
                print(f"   • {conquista}")
                
    def _contar_tarefas_concluidas(self) -> int:
        """Conta o total de tarefas concluídas"""
        total = 0
        for modulo in self.modulos:
            total += sum(1 for t in modulo.tarefas if t.status == Status.CONCLUIDO)
        return total
        
    def _contar_total_tarefas(self) -> int:
        """Conta o total de tarefas"""
        total = 0
        for modulo in self.modulos:
            total += len(modulo.tarefas)
        return total
        
    def _contar_modulos_concluidos(self) -> int:
        """Conta módulos completamente concluídos"""
        total = 0
        for modulo in self.modulos:
            if all(t.status == Status.CONCLUIDO for t in modulo.tarefas):
                total += 1
        return total
        
    def _obter_tarefas_recomendadas(self):
        """Obtém tarefas recomendadas (não concluídas e com dependências satisfeitas)"""
        recomendadas = []
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.status != Status.CONCLUIDO:
                    # Verificar dependências
                    dependencias_satisfeitas = all(
                        self._tarefa_concluida(dep_id) for dep_id in tarefa.dependencias
                    )
                    if dependencias_satisfeitas:
                        recomendadas.append((modulo.id, tarefa))
        return recomendadas
        
    def exibir_modulo(self, modulo_id: int):
        """Exibe detalhes de um módulo específico"""
        modulo = next((m for m in self.modulos if m.id == modulo_id), None)
        if not modulo:
            print(f"❌ Módulo {modulo_id} não encontrado!")
            return
            
        print(f"\n{'='*60}")
        print(f"📚 MÓDULO {modulo.id}: {modulo.titulo}")
        print(f"{'='*60}")
        print(f"📝 {modulo.descricao}")
        print(f"🎯 Objetivo: {modulo.objetivo}")
        print(f"⭐ XP do módulo: {modulo.xp_modulo}")
        
        # Progresso do módulo
        concluidas = sum(1 for t in modulo.tarefas if t.status == Status.CONCLUIDO)
        progresso = (concluidas / len(modulo.tarefas)) * 100
        barra = "█" * int(progresso/5) + "░" * (20 - int(progresso/5))
        
        print(f"\n📊 Progresso do módulo: [{barra}] {progresso:.1f}%")
        print(f"   Tarefas: {concluidas}/{len(modulo.tarefas)} concluídas")
        
        print(f"\n📋 TAREFAS:")
        for i, tarefa in enumerate(modulo.tarefas, 1):
            status_icon = "✅" if tarefa.status == Status.CONCLUIDO else "🔴"
            print(f"   {i}. {status_icon} [{tarefa.id}] {tarefa.titulo}")
            print(f"      Dificuldade: {tarefa.nivel.value}")
            print(f"      XP: {tarefa.xp_recompensa} | Duração: {tarefa.duracao_estimada}h")
            print(f"      Tags: {', '.join(tarefa.tags)}")
            if tarefa.dependencias:
                print(f"      Depende de: {tarefa.dependencias}")
            print()
            
    def exibir_tarefa(self, tarefa_id: int):
        """Exibe detalhes de uma tarefa específica"""
        tarefa_encontrada = None
        modulo_encontrado = None
        
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.id == tarefa_id:
                    tarefa_encontrada = tarefa
                    modulo_encontrado = modulo
                    break
            if tarefa_encontrada:
                break
                
        if not tarefa_encontrada:
            print(f"❌ Tarefa {tarefa_id} não encontrada!")
            return
            
        print(f"\n{'='*60}")
        print(f"📝 TAREFA {tarefa_encontrada.id}: {tarefa_encontrada.titulo}")
        print(f"{'='*60}")
        print(f"📚 Módulo: {modulo_encontrado.titulo}")
        print(f"📖 Descrição: {tarefa_encontrada.descricao}")
        print(f"⚡ Dificuldade: {tarefa_encontrada.nivel.value}")
        print(f"⭐ XP: {tarefa_encontrada.xp_recompensa}")
        print(f"⏱️  Duração estimada: {tarefa_encontrada.duracao_estimada}h")
        print(f"🏷️  Tags: {', '.join(tarefa_encontrada.tags)}")
        print(f"📊 Status: {tarefa_encontrada.status.value}")
        
        if tarefa_encontrada.dependencias:
            print(f"\n🔗 DEPENDÊNCIAS:")
            for dep_id in tarefa_encontrada.dependencias:
                concluida = self._tarefa_concluida(dep_id)
                status = "✅" if concluida else "❌"
                print(f"   {status} Tarefa {dep_id}")
                
        if tarefa_encontrada.status == Status.CONCLUIDO:
            print(f"\n📅 Concluída em: {tarefa_encontrada.data_conclusao}")
            
    def gerar_relatorio(self):
        """Gera um relatório detalhado do progresso"""
        print(f"\n{'='*60}")
        print(f"📈 RELATÓRIO DE PROGRESSO - {self.usuario}")
        print(f"{'='*60}")
        print(f"Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"\n📊 ESTATÍSTICAS GERAIS:")
        print(f"   • Nível: {self.nivel}")
        print(f"   • XP Total: {self.xp_total}")
        print(f"   • Streak atual: {self.streak} dias")
        print(f"   • Tarefas concluídas: {self._contar_tarefas_concluidas()}/{self._contar_total_tarefas()}")
        print(f"   • Módulos completos: {self._contar_modulos_concluidos()}/{len(self.modulos)}")
        
        # Tempo total estimado
        horas_concluidas = sum(
            t.duracao_estimada for modulo in self.modulos 
            for t in modulo.tarefas if t.status == Status.CONCLUIDO
        )
        horas_totais = sum(
            t.duracao_estimada for modulo in self.modulos 
            for t in modulo.tarefas
        )
        
        print(f"   • Horas estudadas: {horas_concluidas}h/{horas_totais}h")
        
        # Progresso por módulo
        print(f"\n📚 PROGRESSO POR MÓDULO:")
        for modulo in self.modulos:
            concluidas = sum(1 for t in modulo.tarefas if t.status == Status.CONCLUIDO)
            total = len(modulo.tarefas)
            progresso = (concluidas / total) * 100 if total > 0 else 0
            barra = "█" * int(progresso/10) + "░" * (10 - int(progresso/10))
            
            status = "✅" if concluidas == total else "🟡" if concluidas > 0 else "🔴"
            print(f"   {status} Módulo {modulo.id}: {modulo.titulo}")
            print(f"      [{barra}] {progresso:.1f}% ({concluidas}/{total} tarefas)")
            
        # Distribuição por dificuldade
        print(f"\n⚡ DISTRIBUIÇÃO POR DIFICULDADE:")
        dificuldades = defaultdict(int)
        for modulo in self.modulos:
            for tarefa in modulo.tarefas:
                if tarefa.status == Status.CONCLUIDO:
                    dificuldades[tarefa.nivel] += 1
                    
        for nivel in NivelDificuldade:
            total = dificuldades.get(nivel, 0)
            print(f"   {nivel.value}: {total} tarefas")
            
        # Próximos passos
        print(f"\n🎯 PRÓXIMOS PASSOS RECOMENDADOS:")
        recomendadas = self._obter_tarefas_recomendadas()
        if recomendadas:
            for i, (modulo_id, tarefa) in enumerate(recomendadas[:5], 1):
                print(f"   {i}. Módulo {modulo_id}: {tarefa.titulo}")
        else:
            print(f"   🎉 Todas as tarefas estão concluídas! Parabéns!")
            
        # Salvar relatório em arquivo
        with open(f'relatorio_{self.usuario}_{datetime.datetime.now().strftime("%Y%m%d")}.txt', 'w') as f:
            f.write(str(self))
            
    def exibir_menu(self):
        """Exibe o menu interativo"""
        while True:
            print(f"\n{'='*60}")
            print(f"🎮 MENU PRINCIPAL - {self.usuario}")
            print(f"{'='*60}")
            print(f"1. 📊 Ver Dashboard")
            print(f"2. 📚 Listar Módulos")
            print(f"3. 📝 Detalhes do Módulo")
            print(f"4. 🔍 Detalhes da Tarefa")
            print(f"5. ✅ Completar Tarefa")
            print(f"6. 📈 Gerar Relatório")
            print(f"7. 🎯 Próximas Tarefas")
            print(f"8. 🏆 Minhas Conquistas")
            print(f"9. 🎲 Simular Exercício NS3")
            print(f"10. 📊 Simular Análise Estatística")
            print(f"0. 🚪 Sair")
            
            escolha = input("\nEscolha uma opção: ")
            
            if escolha == "1":
                self.exibir_dashboard()
                
            elif escolha == "2":
                print(f"\n📚 MÓDULOS DISPONÍVEIS:")
                for modulo in self.modulos:
                    concluidas = sum(1 for t in modulo.tarefas if t.status == Status.CONCLUIDO)
                    status = "✅" if concluidas == len(modulo.tarefas) else "🟡" if concluidas > 0 else "🔴"
                    print(f"   {status} Módulo {modulo.id}: {modulo.titulo}")
                    
            elif escolha == "3":
                try:
                    modulo_id = int(input("Número do módulo: "))
                    self.exibir_modulo(modulo_id)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
                    
            elif escolha == "4":
                try:
                    tarefa_id = int(input("ID da tarefa (ex: 101): "))
                    self.exibir_tarefa(tarefa_id)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
                    
            elif escolha == "5":
                try:
                    tarefa_id = int(input("ID da tarefa para completar: "))
                    self.completar_tarefa(tarefa_id)
                except ValueError:
                    print("❌ Por favor, digite um número válido!")
                    
            elif escolha == "6":
                self.gerar_relatorio()
                print(f"✅ Relatório gerado com sucesso!")
                
            elif escolha == "7":
                print(f"\n🎯 PRÓXIMAS TAREFAS RECOMENDADAS:")
                recomendadas = self._obter_tarefas_recomendadas()
                if recomendadas:
                    for i, (modulo_id, tarefa) in enumerate(recomendadas, 1):
                        print(f"   {i}. Módulo {modulo_id}: [{tarefa.id}] {tarefa.titulo}")
                else:
                    print(f"   🎉 Todas as tarefas estão concluídas!")
                    
            elif escolha == "8":
                print(f"\n🏆 MINHAS CONQUISTAS:")
                if self.conquistas:
                    for i, conquista in enumerate(self.conquistas, 1):
                        print(f"   {i}. {conquista}")
                else:
                    print(f"   😢 Nenhuma conquista ainda. Continue estudando!")
                    
            elif escolha == "9":
                self.simular_ns3()
                
            elif escolha == "10":
                self.simular_analise_estatistica()
                
            elif escolha == "0":
                print(f"\n👋 Até logo, {self.usuario}! Continue estudando!")
                break
                
            else:
                print("❌ Opção inválida! Tente novamente.")
                
    def simular_ns3(self):
        """Simula um exercício de simulação NS3"""
        print(f"\n{'='*60}")
        print(f"🎲 SIMULAÇÃO NS3 - CENÁRIO 5G OPEN RAN")
        print(f"{'='*60}")
        
        print(f"\n📡 Configurando cenário de simulação...")
        time.sleep(1)
        
        # Parâmetros da simulação
        num_cells = random.randint(3, 8)
        num_users = random.randint(20, 100)
        simulation_time = random.randint(30, 180)
        
        print(f"\n⚙️  PARÂMETROS DA SIMULAÇÃO:")
        print(f"   • Células (gNBs): {num_cells}")
        print(f"   • Usuários (UEs): {num_users}")
        print(f"   • Tempo de simulação: {simulation_time}s")
        
        print(f"\n🚀 Iniciando simulação...")
        time.sleep(2)
        
        # Gerar resultados simulados
        resultados = {
            "throughput_medio": random.uniform(100, 500),
            "latencia_media": random.uniform(5, 30),
            "perda_pacotes": random.uniform(0.1, 5.0),
            "handovers": random.randint(10, 50),
            "cobertura": random.uniform(85, 99)
        }
        
        print(f"\n📊 RESULTADOS DA SIMULAÇÃO:")
        print(f"   • Throughput médio: {resultados['throughput_medio']:.2f} Mbps")
        print(f"   • Latência média: {resultados['latencia_media']:.2f} ms")
        print(f"   • Perda de pacotes: {resultados['perda_pacotes']:.2f} %")
        print(f"   • Handovers executados: {resultados['handovers']}")
        print(f"   • Cobertura: {resultados['cobertura']:.2f} %")
        
        print(f"\n🔍 ANÁLISE ESTATÍSTICA:")
        
        # Análise básica
        if resultados['throughput_medio'] > 300:
            print(f"   ✅ Throughput excelente (>300 Mbps)")
        elif resultados['throughput_medio'] > 150:
            print(f"   ⚠️  Throughput aceitável (150-300 Mbps)")
        else:
            print(f"   ❌ Throughput abaixo do esperado (<150 Mbps)")
            
        if resultados['latencia_media'] < 10:
            print(f"   ✅ Latência excelente (<10 ms)")
        elif resultados['latencia_media'] < 20:
            print(f"   ⚠️  Latência aceitável (10-20 ms)")
        else:
            print(f"   ❌ Latência alta (>20 ms)")
            
        # Pergunta de análise
        print(f"\n🤔 PERGUNTA DE ANÁLISE:")
        print(f"   'Como você melhoraria a cobertura de {resultados['cobertura']:.1f}% para >95%?'")
        
        resposta = input("   Sua resposta (pressione Enter para pular): ")
        if resposta:
            print(f"   📝 Resposta registrada: {resposta}")
            
        print(f"\n🎯 DESAFIO COMPLETO! +15 XP (simulado)")
        
    def simular_analise_estatistica(self):
        """Simula uma análise estatística de dados de rede"""
        print(f"\n{'='*60}")
        print(f"📊 SIMULAÇÃO DE ANÁLISE ESTATÍSTICA")
        print(f"{'='*60}")
        
        print(f"\n📈 Gerando dados de métricas de rede...")
        time.sleep(1)
        
        # Gerar dados simulados
        np.random.seed(42)
        n_samples = 1000
        
        dados = {
            'rssi': np.random.normal(-75, 10, n_samples),
            'sinr': np.random.normal(15, 5, n_samples),
            'throughput': np.random.normal(300, 50, n_samples),
            'latencia': np.random.exponential(10, n_samples),
            'usuarios': np.random.poisson(40, n_samples)
        }
        
        df = pd.DataFrame(dados)
        
        print(f"\n📋 ESTATÍSTICAS DESCRITIVAS:")
        print(df.describe().round(2))
        
        print(f"\n🔍 ANÁLISE DE CORRELAÇÃO:")
        correlacao = df.corr()
        print(correlacao.round(3))
        
        print(f"\n📊 PERGUNTAS DE ANÁLISE:")
        perguntas = [
            "1. Qual métrica tem maior variabilidade?",
            "2. RSSI e SINR são altamente correlacionados?",
            "3. Como o número de usuários afeta o throughput?",
            "4. Identifique possíveis outliers na latência."
        ]
        
        for pergunta in perguntas:
            print(f"   {pergunta}")
            
        resposta = input("\n📝 Escolha uma pergunta para responder (1-4): ")
        
        if resposta in ["1", "2", "3", "4"]:
            print(f"\n💡 DICA PARA ANÁLISE {resposta}:")
            dicas = {
                "1": "Observe o desvio padrão de cada coluna.",
                "2": "Verifique o valor da correlação entre RSSI e SINR.",
                "3": "Analise o coeficiente de correlação entre 'usuarios' e 'throughput'.",
                "4": "Valores acima de Q3 + 1.5*IQR são considerados outliers."
            }
            print(f"   {dicas[resposta]}")
            
            input_resposta = input("   Sua resposta: ")
            print(f"   📝 Análise registrada!")
            
        print(f"\n🎯 EXERCÍCIO COMPLETO! +10 XP (simulado)")
        
    def __str__(self):
        """Representação em string do plano"""
        output = []
        output.append(f"Plano de Estudos: {self.usuario}")
        output.append(f"Nível: {self.nivel} | XP: {self.xp_total}")
        output.append(f"Progresso: {self._contar_tarefas_concluidas()}/{self._contar_total_tarefas()} tarefas")
        return "\n".join(output)


def tutorial_rapido():
    """Exibe um tutorial rápido do sistema"""
    print(f"\n{'='*60}")
    print(f"🎮 TUTORIAL RÁPIDO")
    print(f"{'='*60}")
    print(f"\nEste é um sistema gamificado para estudar:")
    print(f"   • Python para Telecom")
    print(f"   • Data Science e Estatística")
    print(f"   • OPEN RAN e xApps")
    print(f"   • Simulação NS3")
    print(f"\n🎯 COMO FUNCIONA:")
    print(f"   1. Complete tarefas para ganhar XP")
    print(f"   2. Suba de nível ao acumular XP")
    print(f"   3. Mantenha sua streak de dias")
    print(f"   4. Desbloqueie conquistas")
    print(f"\n📚 ESTRUTURA:")
    print(f"   • 6 módulos (6 meses)")
    print(f"   • 36 tarefas principais")
    print(f"   • Projetos práticos")
    print(f"   • Simulações interativas")
    print(f"\nVamos começar!")


# Execução principal
if __name__ == "__main__":
    print(f"\n{'='*60}")
    print(f"🚀 PLANO DE ESTUDOS GAMIFICADO v2.0")
    print(f"   Python + Data Science + OPEN RAN + NS3")
    print(f"{'='*60}")
    
    # Configurar usuário
    usuario = input("\n👤 Digite seu nome: ").strip() or "Estudante"
    
    # Tutorial
    ver_tutorial = input("\n📚 Ver tutorial rápido? (s/n): ").lower()
    if ver_tutorial == 's':
        tutorial_rapido()
    
    # Criar e executar plano
    plano = PlanoEstudosGamificado(usuario)
    
    # Verificar streak
    hoje = datetime.datetime.now().date()
    if plano.ultimo_acesso:
        ultimo = datetime.datetime.fromisoformat(plano.ultimo_acesso).date()
        if (hoje - ultimo).days == 1:
            print(f"\n🔥 Streak mantido! +5 XP de bônus!")
            plano.xp_total += 5
        elif (hoje - ultimo).days > 1:
            print(f"\n😢 Streak quebrado após {plano.streak} dias")
            plano.streak = 0
            
    print(f"\n🎮 Bem-vindo(a), {plano.usuario}! Seu progresso foi carregado.")
    
    # Menu principal
    plano.exibir_menu() 
