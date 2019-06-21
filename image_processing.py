
import requests
from PIL import Image
import os

# Create Raw image folder
if not os.path.isdir('images'):
    os.mkdir('images')
if not os.path.isdir('images/raw'):
    os.mkdir('images/raw')


def download_raw_images():
    img_urls = [
        'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcRdvCUO76FCcuTmwwAR6uvZGUI3x2GIfUXHjhYtSwknAMSV4r8sQp9h8AzPzVK6vZGeONL8HmvPqro&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTikUDnmKP5cPsmVfgieS8kslRxyaZWwT455O93GXR7u8OVdPrYz8g_EYAZP0dQlC5cJQnKnKTyLYY&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTz2xyKDfr55EKAFBJYFuAfT94QVdqd_oUQOwcdS_B2h2S2lW4BNzmypuxXdWDf4F4z2mHx014v3Zg&usqp=CAc',
        'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSraDBALOGQZy6paLFL-tnNQurvjyV9QM8fLZCkJhpOAMj8BGQ1rV3GrPUT1Rrv8NhNgzIssXc5D38&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcR7CBqSawdJ2xp8L6GShUfKQmks97kSWNrpOxVRETCwnkfy6seV60hoDi1AdVA4Il0OlYlO4-nAeg&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRNWB6FgbahnHDhOf7rSAUi6ibRd62HzGike9r4FeHXDDyQzm-MtQZBMCk7G_k7-PLj0rEf6lmYVg&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRbYqeEE4nLKDDlTNPMk3wMs0EJp-Gs4oLq75vpRrbyojHhtvH6EFDqeaDT7k0SAb82NFZLOcEFfA&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcR2Rhh6Pslzct3v61rIe8TqwcU-bsmVdqdYMCDUEl1C6PjqqoNmU5QZgokQCHBXmulbAYXymElwTwkBfw&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRCxBP9Rtk4l8rFbervdqmYU34Jrmb-04_AmEfY6u4jInEfQBn7kXSm4Sq7o22X5RcFL44FMSLJb5x7CA&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcTHFQIx8qtJJDJOrKMHFu0-hvMyzO9WqVo3rQkyxoknFLfCiVzo7lq6AsvJjmCyKQa16V69TVHnYiA&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcToulc8csbQ4MRdFd_4t2Cq8xxsHHiHluM2FVyhH4i_hg9-vGofrPugNpMNKUWf_5TwrBJJz8CAdcw&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSQGlN3ST9YrcJqwEYLjGHkVcltEHZzKIShcL78YaZTv_93zUCrdLPcj6Gr4mHBAFlaN8OaykLCLBg&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcS2y5Fnj6neUvsEawhxsDG5-IlRNt9UfbE5fLucusXw9wZbLY6pDi21lKsXkWwvbhrOozCPcM5r9Bw&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQ5RAd6lQ_EjHR_WlDwA9c4zckOBZtQ2f9VOlupVqr71_zO5nLBDGwkRMfQLh8Nzlh8_reO9kkz_aY&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQPuGMbb4-kbFLq27eBwr2IGNUBKiGtFDWzMYEGauD6eywCyM1APQkNjjslooeU_GvO5miv3czA6SM&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRnB9l-yGjAkxGHJDhER23ffScVWAE0QWL40VdiWzPMND9xDt_1g1y4ayOw4qLQTehG8fnMGhGkqTo&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSpjNO64aorW-NpqUsCwsJGGxkrVYryyQbPy4VmBxZx4F1i5FKyvbYSdA7bvoDr1sykICSIOo9fUa9iZg&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRlBxovJ4nGLibtJUuGk2jZbvn0JT_Mv0MYNYMJq3AXBOTZTkgEtoVzigSNivduwX05G6lde0lXKyg&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcTNfB2_bpMXfqGUup1nInchotb7_rkPX4vT6pnJsNQDMMCQj6Q9Tw-WyBgsOvw9n0jLpaE1Y-EyOBI&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRJbBH07Y6eKCgcexJ7M8vqmqUChWYYFSpxXvilXw4U_MiosQ9gRw_AnczlP6jj4fgs-FJgdP-2Uw&usqp=CAc',
        'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQoW9t8gayUP8bUmAU9j5Ns0aF_os2N6Frq8dC2eed2qdsp8SCNGRUs3_o5R-2NA0dCxAy866qv4s4&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRYc8on56EDyDeEheHWC7sAY8Fl4WkB5uCDWaW5d504-0rpwGnEYaNsjnj2O82uIgMwGVsmwqkscw&usqp=CAc',
        'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQ4_V-ZpJ9atZ5tE6XAseeE7N2lAgcQTQLh036JRAt4GGKgzkZWZ4Jk3YBD4s7eeh5WdJHZMxQsakxm&usqp=CAc',
        'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcTTVB9L8OkcHjO0NGb47bQdBtjl5YkkwmuZzaHeHAADoksQUHsmbH6todc_4Di8G3mlzuOpSIbVdA&usqp=CAc',
        'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSXL8-YwGcyVI-tZ-I27M_OTFK8oU3ruQm0yeGMI16RHv57PYl-n5h9ItafAYwcoWlAG1kjliK1cw&usqp=CAc'
    ]

    for i, url in enumerate(img_urls):
        img_data = requests.get(url).content
        with open('images/raw/%.2d.ppm' % i, 'wb') as pic:
            pic.write(img_data)


def process_images(width=30, height=30):
    raw_imgs = os.listdir('images/raw/')
    for filename in raw_imgs:
        img = Image.open('images/raw/%s' % filename)
        img_resized = img.resize((width, height), Image.NEAREST)



if __name__ == '__main__':
    download_raw_images()
    # process_images()