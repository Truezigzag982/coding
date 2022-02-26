def get_results(data):
    length = data[0]
    width = data[1]
    height = data[2]
    surface_area = 2*(length*width + width*height + length*height)
    volume = length*width*height
    return (surface_area, volume)

def main():
    length = input('what is the length: ')
    width = input('what is the width: ')
    height = input('what is the height: ')
    data = (length, width, height)
    print(data)
    results =  get_results(data)
    print(results)
    print('表面积= ', results[0])
    print('体积= ', results[1])

if __name__ == "__main__":
    main()