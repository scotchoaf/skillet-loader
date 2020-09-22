from skilletlib.skilletLoader import SkilletLoader
import click
import oyaml


@click.command()
@click.option("-ip", "--ip_address", help="device ip address", type=str, default='')
@click.option("-u", "--username", help="device username", type=str, default='admin')
@click.option("-p", "--password", help="device password", type=str, default='Paloalto1')
@click.option("-d", "--skillet_dir", help="skillet directory", type=str, default='.')
def cli(ip_address, username, password, skillet_dir):

    sl = SkilletLoader()
    skillets = sl.load_all_skillets_from_dir(skillet_dir)
    d = skillets[0]
    context = dict()
    context['username'] = username
    context['password'] = password
    context['ip_address'] = ip_address
    d.initialize_context(context)
    out = d.execute(context)
    #print(out)

    ignore_fields = ['config', 'device_config_file', 'ip_address','username', 'password']

    for key in d.context:
        if key not in ignore_fields:
            print(f'{key}: {d.context[key]}')


if __name__ == '__main__':
    cli()