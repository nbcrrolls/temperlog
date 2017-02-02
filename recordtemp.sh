#!/bin/bash
/root/temper/temper >> /root/temper/temper.log
tail /root/temper/temper.log | python /root/temper/process.py | nc vi-1.rocksclusters.org 2003
