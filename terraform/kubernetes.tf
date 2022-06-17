terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}


provider "yandex" {
  token                    = "AQAAAAAW-nXoAATuwZSLdRc3KkSFmSyQZya4e6k"
  cloud_id                 = "b1gk9bh4eehkeob0qc5a"
  folder_id                = "b1gtnrjn66uqqg19vb8u"
  zone                     = "ru-central1-a"
}
resource "yandex_kubernetes_cluster" "currencies" {
  network_id = "enpuc6msob1f8s4irbri"
  master {
    regional {
      region = "ru-central1"

      location {
        zone      = "ru-central1-a"
        subnet_id = "e9bfcoingr5dj435lfqm"
      }

      location {
        zone      = "ru-central1-b"
        subnet_id = "e2l50r62r0lok7oqjvfc"
      }

     location {
        zone      = "ru-central1-c"
        subnet_id = "b0cj1fg80tbo7cmb7ces"
    }
  }

#    version   = "1.14"
    public_ip = true

    maintenance_policy {
      auto_upgrade = true

      maintenance_window {
        day        = "monday"
        start_time = "15:00"
        duration   = "3h"
      }

      maintenance_window {
        day        = "friday"
        start_time = "10:00"
        duration   = "4h30m"
      }
    }
  }

  service_account_id      = "ajegmgold6ecpbkncm0b"
  node_service_account_id = "ajegmgold6ecpbkncm0b"

  release_channel = "STABLE"
 }
