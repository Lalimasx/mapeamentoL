from sklearn.tree import DecisionTreeClassifier


def criar_modelo():
    X = [
        [1, 1, 5],
        [1, 2, 8],
        [2, 2, 10],
        [2, 3, 15],
        [3, 3, 20],
        [3, 2, 12],
        [1, 1, 6],
        [2, 1, 10],
        [3, 3, 25],
        [2, 2, 18]
    ]

    y = [
        "Desenvolvimento Web",
        "Desenvolvimento Web",
        "Desenvolvimento Web",
        "Data Science",
        "Inteligência Artificial",
        "Data Science",
        "UX/UI Design",
        "Desenvolvimento Mobile",
        "Inteligência Artificial",
        "Desenvolvimento Mobile"
    ]

    modelo = DecisionTreeClassifier(random_state=42)
    modelo.fit(X, y)

    return modelo


def recomendar_curso(nivel, experiencia, horas_estudo):
    modelo = criar_modelo()

    resultado = modelo.predict([
        [nivel, experiencia, horas_estudo]
    ])

    return resultado[0]