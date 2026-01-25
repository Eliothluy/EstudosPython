"""
📚 EXERCÍCIOS PRÁTICOS PARA O PLANO DE ESTUDOS
"""

import datetime
from main import PlanoEstudosGamificado

class ExerciciosPraticos:
    """Coleção de exercícios práticos para cada módulo"""
    
    @staticmethod
    def modulo1_exercicios():
        """Exercícios do Módulo 1: Python & Estatística"""
        exercicios = {
            "ex1_1": {
                "titulo": "Calculadora de KPIs",
                "descricao": "Crie uma função que calcula: \n"
                           "1. Disponibilidade = (uptime / total_time) * 100\n"
                           "2. Throughput médio\n"
                           "3. Latência p95",
                "dica": "Use dicionários para armazenar métricas"
            },
            "ex1_2": {
                "titulo": "Simulador de RSSI",
                "descricao": "Gere 1000 valores de RSSI com distribuição normal\n"
                           "e calcule média, mediana e desvio padrão",
                "dica": "Use numpy.random.normal"
            },
            "ex1_3": {
                "titulo": "Classificador de Qualidade",
                "descricao": "Classifique células baseado em múltiplas métricas:\n"
                           "- Excelente: SINR > 20 dB AND RSSI > -70 dBm\n"
                           "- Bom: SINR > 10 dB AND RSSI > -80 dBm\n"
                           "- Ruim: outros casos",
                "dica": "Use condições aninhadas"
            }
        }
        return exercicios
    
    @staticmethod
    def modulo2_exercicios():
        """Exercícios do Módulo 2: Data Science"""
        exercicios = {
            "ex2_1": {
                "titulo": "Análise de Dataset Telecom",
                "descricao": "Dado um CSV com métricas, faça:\n"
                           "1. Carregue com pandas\n"
                           "2. Identifique missing values\n"
                           "3. Calcule correlações\n"
                           "4. Crie visualizações",
                "dica": "Use pd.read_csv() e df.corr()"
            },
            "ex2_2": {
                "titulo": "Dashboard Interativo",
                "descricao": "Crie um dashboard com:\n"
                           "1. Gráfico de linhas para throughput\n"
                           "2. Histograma para latência\n"
                           "3. Mapa de calor de correlação",
                "dica": "Use matplotlib e seaborn"
            },
            "ex2_3": {
                "titulo": "Teste de Hipótese",
                "descricao": "Teste se há diferença significativa no throughput\n"
                           "entre células urbanas e rurais (use t-test)",
                "dica": "Use scipy.stats.ttest_ind"
            }
        }
        return exercicios
    
    @staticmethod
    def modulo3_exercicios():
        """Exercícios do Módulo 3: Machine Learning"""
        exercicios = {
            "ex3_1": {
                "titulo": "Previsor de Carga",
                "descricao": "Preveja o número de usuários na próxima hora\n"
                           "usando regressão linear com features:\n"
                           "- Hora do dia\n"
                           "- Dia da semana\n"
                           "- Throughput atual",
                "dica": "Use sklearn LinearRegression"
            },
            "ex3_2": {
                "titulo": "Detector de Anomalias",
                "descricao": "Use Isolation Forest para detectar células\n"
                           "com comportamento anormal nas métricas",
                "dica": "Ajuste o parâmetro contamination"
            },
            "ex3_3": {
                "titulo": "Clustering de Padrões",
                "descricao": "Agrupe células por padrão de uso diário\n"
                           "usando K-means com 4 clusters",
                "dica": "Normalize os dados antes do clustering"
            }
        }
        return exercicios
    
    @staticmethod
    def modulo4_exercicios():
        """Exercícios do Módulo 4: NS3 & OPEN RAN"""
        exercicios = {
            "ex4_1": {
                "titulo": "Script NS3 Básico",
                "descricao": "Crie um script NS3 que:\n"
                           "1. Cria 3 nós (1 servidor, 2 clientes)\n"
                           "2. Estabelece conexão TCP\n"
                           "3. Mede throughput e latência",
                "dica": "Comece com o exemplo first.cc"
            },
            "ex4_2": {
                "titulo": "Simulador 5G",
                "descricao": "Configure um cenário 5G no NS3 com:\n"
                           "- Múltiplas células gNB\n"
                           "- Usuários móveis\n"
                           "- Handovers automáticos",
                "dica": "Use o módulo nr do NS3"
            },
            "ex4_3": {
                "titulo": "Análise de Resultados",
                "descricao": "Analise os traces do NS3 para calcular:\n"
                           "- Taxa de sucesso de handover\n"
                           "- Distribuição de SINR\n"
                           "- QoS por aplicação",
                "dica": "Parseie arquivos .pcap ou .csv"
            }
        }
        return exercicios
    
    @staticmethod
    def modulo5_exercicios():
        """Exercícios do Módulo 5: xApps"""
        exercicios = {
            "ex5_1": {
                "titulo": "API REST para xApp",
                "descricao": "Crie uma API com endpoints:\n"
                           "GET /cells - lista células\n"
                           "POST /decision - recebe decisão\n"
                           "GET /metrics - retorna métricas",
                "dica": "Use FastAPI ou Flask"
            },
            "ex5_2": {
                "titulo": "Containerização",
                "descricao": "Dockerize sua xApp com:\n"
                           "1. Dockerfile multi-stage\n"
                           "2. docker-compose.yml\n"
                           "3. Variáveis de ambiente",
                "dica": "Use imagem python:3.9-slim"
            },
            "ex5_3": {
                "titulo": "Política de Otimização",
                "descricao": "Implemente uma política que:\n"
                           "1. Monitora SINR < 5dB\n"
                           "2. Sugere handover para célula vizinha\n"
                           "3. Logs decisões tomadas",
                "dica": "Use um dicionário para mapear células vizinhas"
            }
        }
        return exercicios
    
    @staticmethod
    def obter_exercicio(modulo_num: int, exercicio_num: int):
        """Retorna um exercício específico"""
        modulos = {
            1: ExerciciosPraticos.modulo1_exercicios,
            2: ExerciciosPraticos.modulo2_exercicios,
            3: ExerciciosPraticos.modulo3_exercicios,
            4: ExerciciosPraticos.modulo4_exercicios,
            5: ExerciciosPraticos.modulo5_exercicios
        }
        
        if modulo_num in modulos:
            exercicios = modulos[modulo_num]()
            chave = f"ex{modulo_num}_{exercicio_num}"
            if chave in exercicios:
                return exercicios[chave]
        
        return {"titulo": "Exercício não encontrado", "descricao": "", "dica": ""}


# Sistema de gamificação adicional
class SistemaGamificacao:
    """Sistema avançado de gamificação"""
    
    def __init__(self):
        self.desafios_diarios = []
        self.leaderboard = {}
        self.eventos_especiais = []
        self._carregar_desafios()
        
    def _carregar_desafios(self):
        """Carrega desafios diários"""
        hoje = datetime.datetime.now().strftime("%Y-%m-%d")
        self.desafios_diarios = [
            {
                "id": 1,
                "titulo": "🎯 Desafio Python: Função Telecom",
                "descricao": "Crie uma função que calcula eficiência espectral",
                "xp": 25,
                "data": hoje,
                "completado": False
            },
            {
                "id": 2,
                "titulo": "📊 Desafio Estatística: Análise KPIs",
                "descricao": "Analise um dataset com pelo menos 3 métricas",
                "xp": 30,
                "data": hoje,
                "completado": False
            },
            {
                "id": 3,
                "titulo": "🤖 Desafio ML: Modelo Simples",
                "descricao": "Treine um modelo de classificação binária",
                "xp": 40,
                "data": hoje,
                "completado": False
            }
        ]
        
    def exibir_desafios_diarios(self):
        """Exibe desafios diários"""
        print(f"\n🔥 DESAFIOS DIÁRIOS - {datetime.datetime.now().strftime('%d/%m/%Y')}")
        print(f"{'='*50}")
        
        for desafio in self.desafios_diarios:
            status = "✅" if desafio["completado"] else "🔴"
            print(f"\n{status} {desafio['titulo']}")
            print(f"   📝 {desafio['descricao']}")
            print(f"   ⭐ Recompensa: {desafio['xp']} XP")
            
    def completar_desafio(self, desafio_id: int):
        """Completa um desafio diário"""
        for desafio in self.desafios_diarios:
            if desafio["id"] == desafio_id:
                if not desafio["completado"]:
                    desafio["completado"] = True
                    print(f"🎉 Desafio completado! +{desafio['xp']} XP")
                    return desafio['xp']
                else:
                    print(f"❌ Desafio já completado!")
                    return 0
        print(f"❌ Desafio não encontrado!")
        return 0


# Script para executar tudo
def main():
    """Função principal para executar o sistema completo"""
    
    print(f"\n{'='*60}")
    print(f"🎮 SISTEMA COMPLETO DE ESTUDOS")
    print(f"{'='*60}")
    
    # Inicializar componentes
    plano = PlanoEstudosGamificado("Estudante")
    exercicios = ExerciciosPraticos()
    gamificacao = SistemaGamificacao()
    
    # Menu interativo
    while True:
        print(f"\n📚 MENU PRINCIPAL")
        print(f"1. Continuar Plano de Estudos")
        print(f"2. Ver Exercícios por Módulo")
        print(f"3. Desafios Diários")
        print(f"4. Simular NS3")
        print(f"5. Simular Análise Estatística")
        print(f"6. Gerar Relatório")
        print(f"0. Sair")
        
        opcao = input("\nEscolha: ")
        
        if opcao == "1":
            plano.exibir_menu()
        elif opcao == "2":
            modulo = int(input("Número do módulo (1-5): "))
            if 1 <= modulo <= 5:
                exercicios_dict = getattr(exercicios, f"modulo{modulo}_exercicios")()
                print(f"\n📚 EXERCÍCIOS MÓDULO {modulo}:")
                for key, ex in exercicios_dict.items():
                    print(f"\n🔹 {ex['titulo']}")
                    print(f"   {ex['descricao']}")
                    print(f"   💡 Dica: {ex['dica']}")
            else:
                print("❌ Módulo inválido!")
        elif opcao == "3":
            gamificacao.exibir_desafios_diarios()
            completar = input("\nCompletar desafio (ID ou 0 para voltar): ")
            if completar != "0":
                try:
                    xp_ganho = gamificacao.completar_desafio(int(completar))
                    plano.xp_total += xp_ganho
                    plano._salvar_progresso()
                except ValueError:
                    print("❌ ID inválido!")
        elif opcao == "4":
            plano.simular_ns3()
        elif opcao == "5":
            plano.simular_analise_estatistica()
        elif opcao == "6":
            plano.gerar_relatorio()
        elif opcao == "0":
            print("\n👋 Até logo! Continue estudando!")
            break
        else:
            print("❌ Opção inválida!")
if __name__ == "__main__":
    main() 
