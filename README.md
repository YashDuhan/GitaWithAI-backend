# Hosting
Backend: Hosted on Vercel at https://gita-with-ai-backend.vercel.app/

# Development Setup Instructions
⚠️ **Important**: This project is configured to run exclusively in a development container environment. Attempting to run it locally without the proper container setup will not work.

## Prerequisites
- An IDE with the Dev Containers extension installed (e.g. Visual Studio Code)
- Docker Desktop installed and running

## Running the Application
1. Open the project in your IDE (preferably VS Code)
2. When prompted, click "Reopen in Container" or press `F1` and select **Dev Containers: Rebuild and Reopen in Container**
3. Once the container is built and running, open a terminal in your IDE and execute the following command:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
   ```

## API Documentation
After the application is running, access the API documentation at:
- **Swagger UI**: [http://localhost/docs](http://localhost/docs)

