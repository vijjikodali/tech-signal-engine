from fastapi import FastAPI
from github_detect import GitHubDetect
from ai_engine import AIEngine
from formatter import Formatter

app = FastAPI()

github = GitHubDetect()
ai = AIEngine()
formatter = Formatter()


@app.get("/health")
def health_check():
    return {"status": "running", "service": "tech-signal-engine"}


@app.get("/github")
def github_trending():
    try:
        data = github.fetch_trending()
        processed = ai.process(data)
        formatted = formatter.format(processed)

        return {
            "source": "github",
            "data": data,
            "processed": processed,
            "formatted": formatted
        }

    except Exception as e:
        return {
            "source": "github",
            "error": str(e)
        }


@app.get("/rss")
def rss_feed():
    try:
        data = github.fetch_latest()  # RSS logic in your engine
        processed = ai.process(data)
        formatted = formatter.format(processed)

        return {
            "source": "rss",
            "data": data,
            "processed": processed,
            "formatted": formatted
        }

    except Exception as e:
        return {
            "source": "rss",
            "error": str(e)
        }