class Parser:

    # Parser header
    def __init__(self, lexer):
        self.next_token = lexer.next_token
        self.token = self.next_token()
        self.level = 0

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
        if self.token.type == 'EOF' or self.token.type == 'volumes' or self.token.type == 'services' or \
                self.token.type == 'version' or self.token.type == 'networks':
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
        elif self.token.type == 'volumes' or self.token.type == 'services' or \
                self.token.type == 'version' or self.token.type == 'networks':
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
            print("Version OK")
            if self.token.type == 'EOF':
                return
            self.take_token('NEWLINE')
            self.level = 0
            self.top_level_element()

        # top_level_element -> services assign newline indentation indentation services_element
        elif self.token.type == 'services':
            self.take_token('services')
            self.take_token('ASSIGN')
            self.take_token('NEWLINE')
            self.level = 1
            self.second_level()
            print("Services OK")
            self.level = 0
            self.top_level_element()

        elif self.token.type == 'volumes':
            self.take_token('volumes')
            self.take_token('ASSIGN')
            self.take_token('NEWLINE')
            self.level = 1
            self.volumes_element()
            print("Volumes ok")
            self.level = 0
            self.top_level_element()

        elif self.token.type == 'networks':
            self.take_token('networks')
            self.take_token('ASSIGN')
            self.take_token('NEWLINE')
            self.level = 1
            self.networks_element()
            print("Networks ok")
            self.level = 0
            self.top_level_element()
        else:
            pass

    def services_element(self):
        if self.level != 0:
            # services_element -> ID assign newline image_prod
            if self.token.type == 'image':
                self.take_token('image')
                self.take_token('ASSIGN')
                self.image_prod()

            # services_element -> ID assign newline build
            elif self.token.type == 'build':
                self.take_token('build')
                self.take_token('ASSIGN')
                self.build_prod()
                self.services_element()

            # services_element -> ID assign newline ports
            elif self.token.type == 'ports':
                self.take_token('ports')
                self.take_token('ASSIGN')
                self.ports_prod()
                self.services_element()

            # services_element -> ID assign newline networks
            elif self.token.type == 'networks':
                self.take_token('networks')
                self.take_token('ASSIGN')
                self.networks_prod()
                self.services_element()

            # services_element -> ID assign newline deploy
            elif self.token.type == 'deploy':
                self.take_token('deploy')
                self.take_token('ASSIGN')
                self.deploy_prod()
                self.services_element()

            elif self.token.type == 'volumes':
                self.take_token('volumes')
                self.take_token('ASSIGN')
                self.volumes_prod()
                self.services_element()
            else:
                pass
        else:
            pass

    def image_prod(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.take_token('INDENTATION')
            self.services_element()
        elif self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.take_token('INDENTATION')
            self.top_level_element()
        else:
            self.error("Epsilon not allowed")

    def build_prod(self):
        self.take_token('ports')
        # TODO
        pass

    def networks_prod(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.services_element()
        elif self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            if self.token.type == 'INDENTATION':
                self.take_token('INDENTATION')
                if self.token.type == 'INDENTATION':
                    self.take_token('INDENTATION')
                    self.take_token('LIST_INDICATOR')
                    self.take_token('SPACE')
                    self.take_token('ID')
                    self.networks_prod()
                else:
                    pass
            else:
                pass

    def ports_prod(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.services_element()
        elif self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.take_token('INDENTATION')
            if self.token.type == 'INDENTATION':
                self.take_token('INDENTATION')
                self.take_token('LIST_INDICATOR')
                self.take_token('SPACE')
                self.take_token('ID')
                self.ports_prod()
            else:
                pass

    def deploy_prod(self):
        self.take_token('NEWLINE')
        if self.token.type == 'INDENTATION':
            self.take_token('INDENTATION')
            if self.token.type == 'INDENTATION':
                self.take_token('INDENTATION')
                if self.token.type == 'INDENTATION':
                    self.take_token('INDENTATION')
                    self.take_token('ID')
                    self.take_token('ASSIGN')
                    self.take_token('ID')
                    self.deploy_prod()
                else:
                    pass
            else:
                pass
        elif self.token.type == 'NEWLINE':
            # error
            pass
        else:
            # exit
            self.level = 0
            pass

    def volumes_prod(self):
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.services_element()
        elif self.token.type == 'NEWLINE':
            self.take_token('NEWLINE')
            if self.token.type == 'INDENTATION':
                self.take_token('INDENTATION')
                self.take_token('INDENTATION')
                if self.token.type == 'INDENTATION':
                    self.take_token('INDENTATION')
                    self.take_token('LIST_INDICATOR')
                    self.take_token('SPACE')
                    self.take_token('ID')
                    self.take_token('ASSIGN')
                    self.take_token('ID')
                    self.volumes_prod()
                else:
                    pass
            else:
                pass

    def volumes_element(self):
        if self.token.type == 'INDENTATION':
            self.take_token('INDENTATION')
            self.take_token('ID')
            self.take_token('ASSIGN')
            if self.token.type != 'EOF':
                self.take_token('NEWLINE')
                self.volumes_element()
            else:
                pass
        else:
            pass

    def networks_element(self):
        if self.token.type == 'INDENTATION':
            self.take_token('INDENTATION')
            self.take_token('ID')
            self.take_token('ASSIGN')
            if self.token.type != 'EOF':
                self.take_token('NEWLINE')
                self.networks_element()
            else:
                print('EOF')
                pass
        else:
            pass

    def second_level(self):
        if self.token.type == 'INDENTATION':
            self.take_token('INDENTATION')
        if self.token.type == 'ID':
            self.take_token('ID')
            self.take_token('ASSIGN')
            self.take_token('NEWLINE')
            self.take_token('INDENTATION')
            self.take_token('INDENTATION')
            self.services_element()
            self.second_level()
        else:
            pass
