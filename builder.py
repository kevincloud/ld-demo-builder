import os
import sys
import randomname
import DemoBuilder


LD_API_KEY = os.environ["LD_API_KEY"]


def usage():
    print("Usage: python builder.py COMMAND")
    print("Commands:")
    print("  build")
    print("  cleanup <project_key>")
    print("Example:")
    print("  python builder.py build")
    sys.exit()


if len(sys.argv) < 2:
    usage()

cmd = sys.argv[1].lower()

match cmd:
    case "build":
        project_key = randomname.get_name()
        project_name = "Coast Demo (" + project_key + ")"
        demo = DemoBuilder.DemoBuilder(LD_API_KEY, project_key, project_name)
        # will eventually be: build_all()
        demo.create_project()
        demo.create_flags()
        demo.create_metrics()
        demo.create_metric_groups()
        print(
            "Project created: "
            + project_name
            + " (Project Key is: "
            + project_key
            + ")"
        )
        print("Client-side SDK key: " + demo.client_id)
    case "cleanup":
        if len(sys.argv) < 3:
            print("Usage: python builder.py cleanup <project_key>")
            sys.exit()
        project_key = sys.argv[2]
        project_name = "Coast Demo (" + project_key + ")"
        demo = DemoBuilder.DemoBuilder(LD_API_KEY, project_key, project_name)
        print(
            "Are you sure you want to delete this project? It will be gone forever and cannot be undone."
        )
        confirm = input("Type 'DELETE' to confirm: ")
        if confirm == "DELETE":
            demo.cleanup()
        else:
            print("Project not deleted.")
    case _:
        usage()
