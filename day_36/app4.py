from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions

# Load the Titanic dataset
X_train, y_train, X_test, y_test = titanic_survive()

# Create and train the RandomForestClassifier model
model = RandomForestClassifier().fit(X_train, y_train)

# Create the ClassifierExplainer
explainer = ClassifierExplainer(
    model, 
    X_test, 
    y_test,
    cats=['Sex', 'Deck', 'Embarked'],
    descriptions=feature_descriptions,
    labels=['Not survived', 'Survived']
)

# Create and run the ExplainerDashboard
ExplainerDashboard(explainer).run()
