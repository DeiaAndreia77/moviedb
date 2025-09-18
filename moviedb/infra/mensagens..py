from typing import Dict, Any

from  flask import current_app
from postmarker.core import PostmarkClient


def enviar_email(destinatario: str,
                 assunto: str,
                 email: str) -> Dict[Any, Any]:

    postmark =  PostmarkClient(server_token=current_app.config["SERVER_TOKEN"],
                               account_token=current_app.config['ACCOUNT_TOKER'])
    resultado = postmark.emails.send(
        From='a.perpetua@aluno.ifsp.edu.br',
        To=destinatario,
        Subject=assunto,
        TextBady=email
)
    return resultado

