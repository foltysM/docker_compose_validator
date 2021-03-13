class Parser:


# TODO ogarnac liczbe indentation

    # Parser header
    def __init__(self, lexer):
        self.next_token = lexer.next_token
        self.token = self.next_token()

    def take_token(self, token_type):
        if self.token.type != token_type:
            self.error("Unexpected token: %s" % token_type)
        if token_type != 'EOF':
            self.token = self.next_token()

    def error(self, msg):
        raise RuntimeError('Parser error, %s' % msg)

    # Parser body

    def start(self):
        # start -> program EOF
        if self.token.type == 'EOF' or self.token.type == 'volumes' or self.token.type == 'services' or self.token.type == 'version' or self.token.type == 'networks':
            self.program()
            self.take_token('EOF')
        else:
            self.error("Epsilon not allowed")

    def program(self):
        # program -> newline program
        if self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            self.program()
        # program -> top_level_element program
        elif self.token.type == 'volumes' or self.token.type == 'services' or self.token.type == 'version' or self.token.type == 'networks':
            self.top_level_element()
            self.program()
        else:
            pass

    def top_level_element(self):
        # top_level_element -> version assign ID NEWLINE top_level_element
        if self.token.type == 'version':
            self.take_token('version')
            self.take_token('ASSIGN')
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.top_level_element()
            print("top level element OK")
        # top_level_element -> services assign newline indentation indentation services_element
        elif self.token.type == 'services':
            self.take_token('services')
            self.take_token('ASSIGN')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.services_element()
            pass

    def version(self):
        pass

    def assign_prod(self):
        pass

    def services_element(self):
        self.take_token('ID')
        self.take_token('ASSIGN')
        self.take_token('NEWLINE')
        self.take_token('INDENTATION')
        # services_element -> ID assign newline image_prod
        if self.token.type == 'image':
            self.image_prod()
        # services_element -> ID assign newline build
        elif self.token.type == 'build':
            self.build_prod()
        # services_element -> ID assign newline ports
        elif self.token.type == 'ports':
            self.ports_prod()
        # services_element -> ID assign newline networks
        elif self.token.type == 'networks':
            self.networks_prod()
        # services_element -> ID assign newline deploy
        elif self.token.type == 'deploy':
            self.deploy_prod()
        else:
            self.error("Epsilon not allowed")

    def image_prod(self):
        self.take_token('image')
        if self.token.type == 'ASSIGN':
            self.take_token('ASSIGN')
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.services_element()
        elif self.token.type == 'NEWLINE':
            self.take_token('ASSIGN')
            self.take_token('INDENTATION')
            self.top_level_element()
        else:
            self.error("Epsilon not allowed")

    def build_prod(self):
        # TODO
        pass

    def ports_prod(self):
        # TODO
        pass

    def networks_prod(self):
        pass

    def deploy_prod(self):
        pass
            