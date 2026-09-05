from django.contrib.auth.models import Group,Permission

def create_g_p(sender,**kwargs):
    try:
    # creating groups
        reader_group,mode = Group.objects.get_or_create(name="READERS")
        editor_group,mode = Group.objects.get_or_create(name="EDITORS")
        author_group,mode = Group.objects.get_or_create(name="AUTHORS")

    # creating permissions

        r_permissions=[
            Permission.objects.get(codename="view_posts")
        ]

        data,mode=Permission.objects.get_or_create(codename="can_publish",name="post can publish",content_type_id=7)

        e_permissions = [
            data,
            Permission.objects.get(codename="add_posts"),
            Permission.objects.get(codename="delete_posts"),
            Permission.objects.get(codename="change_posts")
        ]

        a_permissions = [
            Permission.objects.get(codename="add_posts"),
            Permission.objects.get(codename="delete_posts"),
            Permission.objects.get(codename="change_posts")

        ]


        # connecting permissions to groups

        reader_group.permissions.set(r_permissions)
        editor_group.permissions.set(e_permissions)
        author_group.permissions.set(a_permissions)
    except Exception as e:
        print("Error Brooo",e)

print("Done Mamamaaaa")