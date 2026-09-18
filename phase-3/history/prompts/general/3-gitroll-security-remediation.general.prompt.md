---
id: 3
title: GitRoll Security Issues Remediation
stage: general
date: 2026-09-18
surface: agent
model: z-ai/glm-5.3-flash
feature: none
branch: main
user: unknown
command: fix-security-issues
labels: ["security", "secrets", "kubernetes", "gitroll", "remediation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - db_url.txt (deleted)
 - .gitignore
 - frontend/.gitignore
 - .env.example
 - backend/.env.example
 - frontend/.env.example
 - backend/src/mcp_server/config.py
 - backend/src/services/auth_service.py
 - docker-compose.yml
 - todo-backend-deployment.yaml
 - todo-frontend-deployment.yaml
 - k8s/charts/todo-app/values.yaml
 - k8s/charts/todo-app/templates/backend-deployment.yaml
 - k8s/charts/todo-app/templates/frontend-deployment.yaml
tests:
 - backend pytest suite (15 passed)
---

## Prompt

analyze the project quickly

Fix all GitRoll security issues in this repository.1. Remove the hardcoded PostgreSQL password from the code, move credentials to environment variables, and ensure secrets are gitignored. Rotate the exposed password if necessary.2. For Kubernetes resources, disable `automountServiceAccountToken` when Kubernetes API access is not required; otherwise configure proper RBAC.3. Add appropriate memory requests and limits to every flagged container.4. Check the entire repo for similar issues and fix them consistently.5. Do not change application functionality. After fixing, verify the repo has no remaining GitRoll issues.

## Response snapshot

Full security remediation executed across 6 areas:

1. **Secrets removal**: Deleted `db_url.txt` (contained live Neon password `npg_...`, was git-tracked) from index and disk; added it plus `*.pem`, `*.key`, `secrets/` to `.gitignore` with `!.env.example` negation. Created `.env.example` templates at root, `backend/`, and `frontend/` documenting all required vars without real values. Removed hardcoded Neon connection string from `backend/src/mcp_server/config.py` and insecure JWT fallback (`fallback_secret_key_for_dev`) from `backend/src/services/auth_service.py` — both now require env vars with no defaults (lazy properties raising RuntimeError with clear messages).

2. **K8s service account tokens**: Set `automountServiceAccountToken: false` on all 3 Deployments (root manifests + Helm templates for both frontend and backend; chart also has ServiceAccount automount=false via values). Neither service uses the K8s API.

3. **Memory resources**: Added `requests: memory 256Mi/cpu 100m` + `limits: memory 512Mi/cpu 500m` to all 4 containers (frontend/backend in both root manifests and Helm values).

4. **Repo-wide sweep**: Fixed Helm values placeholder secrets (`your-jwt-secret` etc.) via `existingSecret: todo-backend-secrets` secretKeyRef pattern; parameterized `docker-compose.yml` credentials with `${POSTGRES_PASSWORD:?}` fail-fast required vars (no defaults); moved frontend GEMINI key from plaintext env value to secretKeyRef in root manifest.

5. **No functional changes**: Backend pytest suite passes 15/15. Only config/security surface touched.

6. **Verification**: Secret-pattern grep (npg_/AIza/sk-/ghp_/xox tokens, postgres URL credentials, insecure defaults) returns only placeholder docs (`.env.example` files, spec quickstart docs, compose comments). `git ls-files` shows no tracked secret files. All automount flags confirmed false; memory resources confirmed in all manifests.

⚠️ **Rotation required**: The Neon password was exposed in git history (commit 83f70c4) and must be rotated in the Neon Console. History rewrite (git filter-repo/BFG) recommended but user decision.

## Outcome

- ✅ Impact: All GitRoll security issues fixed; no remaining secret leaks in working tree
- 🧪 Tests: 15 passed (backend pytest)
- 📁 Files: 14 modified/deleted/created
- 🔁 Next prompts: rotate Neon password; optionally rewrite git history
- 🧠 Reflection: Root-cause fix was moving secret loading to env-only with fail-fast validation, preserving test behavior via central Settings

## Evaluation notes (flywheel)

- Failure modes observed: Initial `os.environ[...]` approach broke pytest import-time; fixed with lazy properties + central Settings lookup
- Graders run and results (PASS/FAIL): PASS (15/15 tests, secret grep clean)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
