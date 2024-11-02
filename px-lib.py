function files_changed() {
  local latter_commit=$1
  local former_commit=$2
  local files=("${@:3}")


  for file in $(git diff --name-only "$former_commit" "$latter_commit"); do
    echo "Checking file $file"
        for pattern in "${files[@]}"; do
            if [[ "$file" == $pattern ]]; then
                echo "File $file changed, matched by pattern $pattern"
                return 0
            else
        echo "File $file did not match pattern $pattern"
      fi
        done
    done

    echo "No files changed"
    return 1
}
