# MyApp — Pipeline CI/CD (Python / Flask)

## Fonctionnement du pipeline
Chaque push sur `main` déclenche GitHub Actions :
1. **unit-tests** : installe les dépendances Python et lance `pytest tests/` (Flask test client).
2. **e2e-tests** : démarre l'app Flask localement (`python app.py`) puis lance `pytest test_e2e.py` avec `requests`, qui teste `/health` et `/api/greet/<name>`.
3. **build-and-push** : build l'image Docker et la pousse sur Docker Hub (tags `latest` + SHA du commit), uniquement si les deux jobs précédents réussissent.
4. **deploy** : se connecte en SSH à la VM Azure, tire la nouvelle image, relance le conteneur via `docker compose up -d` (idempotent), puis vérifie `/health` sur l'IP publique.

## Déclenchement du déploiement
Automatique à chaque `git push origin main`. Aucune action manuelle requise.

## Choix techniques
- **Flask + Gunicorn** : app Python légère, endpoint `/health` dédié au monitoring.
- **Pytest** : utilisé à la fois pour les tests unitaires (test client Flask) et les tests E2E (requêtes HTTP réelles via `requests`), pour rester 100% Python.
- **Docker multi-tag** (`latest` + SHA) : traçabilité des versions déployées.
- **docker compose + nom de conteneur fixe (`myapp`)** : garantit l'idempotence du déploiement.
- **GitHub Secrets** : aucun identifiant en clair (token Docker Hub, clé SSH, IP VM).

## Accès à l'application
http://20.56.74.49:2005