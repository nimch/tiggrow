# https://just.systems/man/en/

# REQUIRES
find := require("find")
rm := require("rm")
uv := require("uv")

# SETTINGS
REPOSITORY := "tiggrow_app"
SOURCES := "src"
TESTS := "tests"
INPUT_CSS_PATH := "tiggrow_app/static/src"
OUTPUT_CSS_PATH := "tiggrow_app/static/css"
set dotenv-load := true

# display help information
default:
    @just --list

# IMPORTS
# import 'just_tasks/check.just'
# import 'just_tasks/clean.just'
# import 'just_tasks/commit.just'
import 'just_tasks/css.just'
# import 'just_tasks/doc.just'
# import 'just_tasks/docker.just'
# import 'just_tasks/format.just'
# import 'just_tasks/install.just'
# import 'just_tasks/launch.just'
# import 'just_tasks/package.just'
