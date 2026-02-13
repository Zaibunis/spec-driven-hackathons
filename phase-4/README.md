# Phase-IV: Local Kubernetes Deployment (Todo Chatbot)

## 🎯 Objective
Deploy the Phase-III Todo Chatbot on a local Kubernetes cluster using Minikube and Helm charts, following a cloud-native DevOps workflow.

## ✅ Features
- **Cloud-Native Deployment**: Containerized application deployed on local Kubernetes
- **Helm Package Management**: Deploy and manage application using Helm charts
- **Local Development Environment**: Minikube-based Kubernetes cluster for development
- **AI-Powered Chatbot**: Gemini-powered AI assistant integrated with todo functionality
- **Multi-User Support**: Each user has their own secure todo lists
- **Responsive Web Interface**: Modern UI built with Next.js App Router
- **Secure Authentication**: JWT-based authentication using Better Auth
- **Persistent Storage**: Data stored in Neon Serverless PostgreSQL

## ✅ Technology Stack

| Component | Technology / Tool |
|-----------|------------------|
| Containerization | Docker (Docker Desktop), Gordon AI |
| Kubernetes Cluster | Minikube |
| Package Manager | Helm Charts |
| AI DevOps Assistance | Claude Code, kubectl-ai, Kagent |
| Application | Phase-III Todo Chatbot (Frontend + Backend) |

### Frontend
- **Framework**: Next.js 16+ (App Router)
- **Styling**: Tailwind CSS
- **State Management**: React Hooks
- **Authentication**: Better Auth client-side integration

### Backend
- **Framework**: Python FastAPI
- **ORM**: SQLModel (SQLAlchemy-based)
- **Authentication**: Better Auth with JWT verification
- **AI Integration**: Google Generative AI (Gemini)

### Database
- **Primary DB**: Neon Serverless PostgreSQL
- **ORM**: SQLModel for database modeling and queries

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Minikube (local Kubernetes)
- **Package Management**: Helm Charts
- **AI DevOps Tools**: Claude Code, kubectl-ai, Kagent

## 🏗️ Architecture

### Services
1. **Frontend Service** (`todo-app-frontend`)
   - Port: 3000
   - Next.js application serving the user interface
   - Communicates with backend via REST API
   - Accessible via: `minikube service todo-app-frontend`

2. **Backend Service** (`todo-app-backend`)
   - Port: 8000
   - FastAPI application providing REST endpoints
   - Handles authentication, data persistence, and AI integration
   - Accessible via: `minikube service todo-app-backend`

3. **Database Service** (`db`)
   - Port: 5432
   - PostgreSQL database for persistent storage
   - Neon Serverless for scalable database infrastructure

### Authentication Flow
1. User registers/signs in via Better Auth
2. Session is created with JWT token
3. Frontend includes JWT in `Authorization: Bearer <token>` header
4. Backend verifies JWT signature and scopes data to authenticated user

## 📁 Project Structure
```
├── backend/                 # Python FastAPI backend
├── frontend/                # Next.js frontend application
├── k8s/                     # Kubernetes deployment manifests
├── specs/                   # Specification documents
├── history/                 # Prompt history records
├── docker-compose.yml       # Docker Compose configuration
├── package.json             # Root dependencies
├── CLAUDE.md               # Claude Code rules and guidelines
├── todo-backend-deployment.yaml    # Backend K8s manifest (todo-app-backend)
├── todo-frontend-deployment.yaml   # Frontend K8s manifest (todo-app-frontend)
└── README.md               # This file
```

## 🔧 Setup Instructions

### Prerequisites
- Docker Desktop
- Minikube
- Helm
- kubectl
- Node.js (for local development)
- Python 3.11+ (for local development)

### Local Kubernetes Setup
1. Start Minikube:
   ```bash
   minikube start
   ```

2. Enable required Minikube addons:
   ```bash
   minikube addons enable ingress
   minikube addons enable dashboard
   ```

3. Build Docker images for the application:
   ```bash
   eval $(minikube docker-env)
   docker build -t todo-frontend ./frontend
   docker build -t todo-backend ./backend
   ```

### Helm Chart Deployment
1. Create Helm chart structure:
   ```bash
   helm create todo-chatbot
   ```

2. Update the Helm chart templates with your deployment configurations

3. Install the Helm chart:
   ```bash
   helm install todo-chatbot ./todo-chatbot
   ```

### Alternative: Direct Kubectl Deployment
1. Apply Kubernetes manifests directly:
   ```bash
   kubectl apply -f k8s/
   ```

2. Verify deployment:
   ```bash
   kubectl get pods
   kubectl get services
   ```

### Access the Application
- Get the Minikube IP: `minikube ip`
- Access the frontend service through the exposed port
- Or use `minikube service todo-frontend-service` to open in browser

### Successfully Deployed Services
After deployment, the following services are accessible:

**Frontend Service:**
- External URL: `http://192.168.49.2:30030`
- Local Tunnel: `http://127.0.0.1:61353`
- Command: `minikube service todo-app-frontend`

**Backend Service:**
- External URL: `http://192.168.49.2:30080`
- Local Tunnel: `http://127.0.0.1:50953`
- Command: `minikube service todo-app-backend`

## 🤖 AI DevOps Workflow
This project leverages AI-assisted DevOps tools:
- **Claude Code**: Automated code generation and deployment planning
- **kubectl-ai**: AI-powered kubectl commands
- **Kagent**: Kubernetes automation agent

## 📊 Kubernetes Resources
The deployment includes:
- Deployments for frontend and backend services
- Services for internal and external communication
- ConfigMaps for configuration management
- Secrets for sensitive data (API keys, passwords)
- PersistentVolumeClaims for data persistence (if needed)

## 🚀 Deployment Commands
```bash
# Install the application using Helm
helm install todo-chatbot-release ./charts/todo-chatbot

# Upgrade the application
helm upgrade todo-chatbot-release ./charts/todo-chatbot

# Uninstall the application
helm uninstall todo-chatbot-release
```

## 🔍 Monitoring and Debugging
- Access Kubernetes dashboard: `minikube dashboard`
- View pod logs: `kubectl logs <pod-name>`
- Execute commands in pods: `kubectl exec -it <pod-name> -- /bin/sh`

## 🔄 Development Workflow
This project follows a cloud-native DevOps workflow:
1. Develop and test locally with Docker Compose
2. Create Helm charts for Kubernetes deployment
3. Deploy to local Minikube cluster
4. Use AI-assisted tools for deployment optimization
5. Iterate and improve deployment configurations

## 🛡️ Security Features
- Kubernetes RBAC for access control
- Encrypted secrets management
- Network policies for service communication
- JWT-based authentication with Better Auth
- Secure API communication with token validation

## 🤖 AI Integration
The application features AI-powered capabilities using Google's Gemini model:
- Natural language processing for todo creation
- Smart suggestions and categorization
- Conversational interface for task management
- AI-assisted DevOps operations

## 📝 Contributing
1. Follow the cloud-native DevOps workflow
2. Use Helm charts for consistent deployments
3. Leverage AI-assisted tools for development and deployment
4. Test changes in local Minikube environment before applying to production

## 📄 License
[Specify license information here]

## 📞 Contact
For questions or support, please contact the development team.