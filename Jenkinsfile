node {
  checkout scm
  docker.withRegistry('https://registry.hub.docker.com','mydockercreds') {
  def customImage = docker.build("random")
  customImage.push()
  }
}
