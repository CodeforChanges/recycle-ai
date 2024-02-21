from typing_extensions import Annotated
import typer

from recycle_ai.message_queue import MessageQueue
from recycle_ai.model.garbage_classification import GarbageClassification

app = typer.Typer()


@app.command()
def serve(
    url: Annotated[
        str, typer.Argument(envvar="RECYCLE_AI_MQ_URL")
    ] = "amqp://guest:guest@rabbitmq:5672/"
):
    print("[INFO] start ai inference server")

    model = GarbageClassification()

    mq = MessageQueue(url, model)
    mq.start_consuming()

    print("[WARN] the program exited")
