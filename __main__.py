import pexpect
from time import sleep


def exibir_banner():
    VERMELHO = "\033[91m"
    RESET = "\033[0m"
    
    # Linhas de rodapé estilizadas em vermelho
    print(VERMELHO + "}-[" + "―" * 20 + " {+} Coded By GhostXYZ {+} " + "―" * 20 + "]-{" + RESET)
    print(VERMELHO + "}-[" + "―" * 18 + " {+} https://github.com/max1337xyz {+} " + "―" * 18 + "]-{" + RESET)
    print()


def automatizar_set(senha_kali="123"):
    """
    Automatiza a navegação inicial no Social-Engineer Toolkit (SET) 
    para configurar um ataque de Credential Harvester simulado.

    Esta função inicializa o setoolkit com privilégios de superusuário (sudo),
    passa pela autenticação automaticamente utilizando a biblioteca pexpect,
    e interage com os menus de texto para selecionar os vetores de ataque web
    e a template desejada.

    Args:
        senha_kali (str): A senha de root/sudo do sistema operacional (Kali Linux).

    Raises:
        pexpect.ExceptionPexpect: Se ocorrer algum erro de tempo limite (timeout) 
            ao aguardar os prompts do terminal ou se o processo falhar ao iniciar.

    Example:
        >>> automatizar_set("minha_senha_segura")
    """


    try:
        # Inicia o comando com sudo e -S para a senha, chamando o setoolkit
        print("[*] Iniciando o SET...")
        sleep(2)
        
        filho = pexpect.spawn("sudo -S setoolkit", encoding="utf-8")

        filho.expect("password.*:")
        filho.sendline(senha_kali)

        filho.expect("Select from the menu:")
        filho.sendline("1")


        filho.expect("Select from the menu:")
        filho.sendline("2")


        filho.sendline("3")


        filho.sendline("1")

        filho.sendline("")

        filho.sendline("3")

        filho.interact()

    except pexpect.ExceptionPexpect as e:
        
        print(f"[-] Ocorreu um erro na automação: {e}")

if __name__ == "__main__":
    senha = input("Digite Sua Senha De Su ")
    exibir_banner()
    automatizar_set(senha_kali=senha)