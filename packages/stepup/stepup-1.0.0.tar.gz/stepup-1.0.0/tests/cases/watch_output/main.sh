#!/usr/bin/env -S bash -x
# Exit on first error and cleanup.
set -e
trap 'kill $(pgrep -g $$ | grep -v $$) > /dev/null 2> /dev/null || :' EXIT
xargs rm -rvf < .gitignore

# Run the example
stepup -w 1 plan.py & # > current_stdout.txt &

# Get the graph after completion of the pending steps.
python3 - << EOD
from stepup.core.interact import *
wait()
graph("current_graph_01.txt")
EOD

# Check files that are expected to be present and/or missing.
[[ -f plan.py ]] || exit -1
[[ -f input.txt ]] || exit -1
[[ -f output.txt ]] || exit -1

# Remove a built file and rerun.
rm output.txt
python3 - << EOD
from stepup.core.interact import *
watch_del("output.txt")
run()
wait()
graph("current_graph_02.txt")
join()
EOD

# Wait for background processes, if any.
wait $(jobs -p)

# Check files that are expected to be present and/or missing.
[[ -f plan.py ]] || exit -1
[[ -f input.txt ]] || exit -1
[[ -f output.txt ]] || exit -1
