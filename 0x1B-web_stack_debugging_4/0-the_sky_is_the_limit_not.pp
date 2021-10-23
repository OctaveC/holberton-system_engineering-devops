#Fix failling requests

exec {'using sed to increase limit':
  path    => ['/usr/local/bin', '/bin'],
  command => "sudo sed -i 's/15/4000/' /etc/default/nginx",
}

exec {'nginx restart':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}
