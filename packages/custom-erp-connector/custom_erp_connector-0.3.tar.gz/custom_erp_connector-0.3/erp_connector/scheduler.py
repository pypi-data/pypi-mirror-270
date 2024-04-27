import argparse
from apscheduler.schedulers.background import BackgroundScheduler
from erp_connector.service.connector_service import process_connector
import time
from erp_connector.service.sqlite_service import create_table


def run_scheduler(config_path):
    create_table()
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(process_connector, 'interval', minutes=1, max_instances=1,args=(config_path,))
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ERP Connector Scheduler')
    parser.add_argument('config_path', type=str, help='Path to configuration file')
    args = parser.parse_args()
    run_scheduler(args.config_path)
