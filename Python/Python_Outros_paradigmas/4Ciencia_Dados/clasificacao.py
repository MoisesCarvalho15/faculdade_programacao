from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.svm import SVC

### Pré-processamento ###
# Coleta e Integração
iris = load_iris() # obtendo o dataset de flores

caracteristicas = iris.data
rotulos = iris.target # acessando os atributos

print(f'Características: \n{caracteristicas[:2]}')
print(f'Rótulos: \n{rotulos[:2]}')
print('#'*40)

# Partição dos dados
carac_treino, carac_teste, rot_treino, rot_teste = train_test_split(caracteristicas, rotulos)

### Mineração ###
# Árvore de Decisão
arvore = DecisionTreeClassifier(max_depth=2)
arvore.fit(X=carac_treino, y=rot_treino)

rot_preditos = arvore.predict(carac_teste)
acuracia_arvore = accuracy_score(rot_teste, rot_preditos)

### Máquina de Vetor Suporte ###
clf = SVC()
clf.fit(X=carac_treino, y=rot_treino)

rot_preditos_svm = clf.predict(carac_teste)
acuracia_svm = accuracy_score(rot_teste, rot_preditos_svm)

### Pós-processamento ###
print(f'Acurácia Árvore de Decisão: {round(acuracia_arvore, 5)}')
print(f'Acurácia SVM: {round(acuracia_svm, 5)}')
print('#'*40)

r = export_text(arvore, feature_names=iris['feature_names'])
print('Estrutura da árvore')
print(r)