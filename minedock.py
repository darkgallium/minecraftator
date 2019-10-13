import docker

def new_minecraft(name, op):

    client = docker.from_env()
    # itzg/minecraft-server

    exposed_port = 0

    with open("port.txt", "r") as f:

        exposed_port = int(f.readline())
        
        env = [
                "EULA=TRUE",
                "ONLINE_MODE=FALSE",
                "OPS={}".format(op),
                "MOTD=Salt powered",
                "ENABLE_RCON=false",
                "SERVER_PORT=25565"
        ]

        client.containers.run("itzg/minecraft-server:latest",
                              name="mc_"+name,
                              environment=env,
                              ports={'25565/tcp': exposed_port},
                              detach=True)


    with open("port.txt", "w") as f:
        f.write("{}".format((exposed_port+1)))

    return exposed_port
