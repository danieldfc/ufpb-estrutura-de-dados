class SelectionSort:

  def sort(self, arr):
    for index in range(0, len(arr)):
      min_index = index

      for rigth in range(index + 1, len(arr)):
        if arr[rigth] < arr[min_index]:
          min_index = rigth

      arr[index], arr[min_index] = arr[min_index], arr[index]

    return arr
