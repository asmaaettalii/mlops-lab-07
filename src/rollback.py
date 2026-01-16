from __future__ import annotations

"""
Script utilitaire de gestion du Model Registry via MLflow.

Objectif principal :
- Lister les versions du modele enregistre dans MLflow.
- Mettre a jour l'alias "production" pour activer :
  - une version specifique (via target),
  - ou, par defaut, la version precedente (rollback).

Le registry local (metadata.json, current_model.txt) n'est plus utilise.
MLflow devient la source de verite.
"""

from typing import Optional

import mlflow
from mlflow.tracking import MlflowClient

MODEL_NAME = "churn_model"
ALIAS = "production"


def _list_versions(client: MlflowClient) -> list[int]:
    versions = client.search_model_versions(f"name='{MODEL_NAME}'")
    return sorted({int(v.version) for v in versions})


def _get_current_version(client: MlflowClient) -> Optional[int]:
    try:
        mv = client.get_model_version_by_alias(MODEL_NAME, ALIAS)
        return int(mv.version)
    except Exception:
        return None


def _set_alias(client: MlflowClient, version: int) -> None:
    client.set_registered_model_alias(MODEL_NAME, ALIAS, str(version))


def main(target: Optional[str] = None) -> None:
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    client = MlflowClient()

    versions = _list_versions(client)
    if not versions:
        raise FileNotFoundError(
            f"Aucune version MLflow trouvee pour le modele '{MODEL_NAME}'. "
            "Lancer train.py au moins une fois."
        )

    if target is not None:
        try:
            v = int(target)
        except ValueError as e:
            raise ValueError("target doit etre un numero de version (ex: '2').") from e

        if v not in versions:
            raise ValueError(f"Version inconnue : v{v}. Versions disponibles : {versions}")

        _set_alias(client, v)
        print(f"[OK] activation => {MODEL_NAME}@{ALIAS} = v{v}")
        return

    current = _get_current_version(client)
    if current is None:
        current = versions[-1]

    idx = versions.index(current)
    if idx == 0:
        raise ValueError(
            f"Rollback impossible : {MODEL_NAME}@{ALIAS} est deja sur "
            f"la plus ancienne version (v{current})."
        )

    previous = versions[idx - 1]
    _set_alias(client, previous)
    print(f"[OK] rollback => {MODEL_NAME}@{ALIAS} : v{current} -> v{previous}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else None)
