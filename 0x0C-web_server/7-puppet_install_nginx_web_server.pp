# Puppet task configuration

exec {'apt-update':
    command => '/usr/bin/env apt-get -y update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Package['apache2.2-common']
}

service {'nginx':
  ensure  =>  'running',
  require => file_line['perform a redirection'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Holberton School',
  require =>  Package['nginx']
}

file_line { 'redirect':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  line    => 'rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  after   => 'root /var/www/html;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
