def remove_dups(str):
  # where and when
  cur_dup = ''
  idx = 0
  start = idx - len(cur_dup)
  end = idx

  while idx < len(str):

    '''-Initiate length check-
    If the length of cur_dup == 0 then this it's empty,
      this iteration is the initial value.
    Otherwise, check if this iteration == the first character
      of cur_dup. If so, add value to the cur_dup string'''
    if len(cur_dup) == 0:
      cur_dup = str[idx]
    else:
      if str[idx] == cur_dup[0]:
        cur_dup += str[idx]
      '''If this iteration != cur_dup[0], check cur_dup's length
      If > 3, take parameter string - cur_dup and recursively pass it through again
      If not, no removal needed so add this iteration as the new initiatal value'''
      else:
        if len(cur_dup) > 2:
          start = idx - len(cur_dup)
          end = idx
          s = str[:start] + '' + str[end:]
          return remove_dups(s)

        else:
          cur_dup = str[idx]
    '''Increase idx to iterate'''
    idx += 1

  '''Final pass, if len(cur_dup) > 2, remove
  it and return the rest of the string. Otherwise
  it's fine and just return the string as is'''
  if len(cur_dup) > 2:
    start = idx - len(cur_dup)
    end = idx
    return str[:start]
  else:
    return str

print(remove_dups('bbbbccbbbc'))