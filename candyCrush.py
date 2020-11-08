def remove_dups(str):
  # where and when
  cur_dup = ''
  idx = 0
  start = idx - len(cur_dup)
  end = idx

  while idx < len(str):

    if len(cur_dup) == 0:
      cur_dup = str[idx]
    else:
      if str[idx] == cur_dup[0]:
        cur_dup += str[idx]
      else:
        if len(cur_dup) > 2:
          start = idx - len(cur_dup)
          end = idx
          s = str[:start] + '' + str[end:]
          return remove_dups(s)

        else:
          cur_dup = str[idx]
    idx += 1

  if len(cur_dup) > 2:
    start = idx - len(cur_dup)
    end = idx
    return str[:start]
  else:
    return str

print(remove_dups('bbbbccbbbc'))