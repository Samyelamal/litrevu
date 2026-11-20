from django.contrib import admin

from reviews.models import Review, Ticket, UserBlocks, UserFollows


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'time_created')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('headline', 'rating', 'ticket', 'user', 'time_created')


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user')


@admin.register(UserBlocks)
class UserBlocksAdmin(admin.ModelAdmin):
    list_display = ('user', 'blocked_user')
