$(document).ready(function() {
    $(".like_button").click(function(event) {
        // Raises the like counter by 1 when a unique user clicks the like button, and vice versa

        // Get required data for a like
        let target = $(event.currentTarget);
        let twit_id = target.data("id");
        let twit_action = target.data("action");
        let twit_like_url = target.data("like-url");

        // Get elements for like button icon and count
        let like_icon = target.find(".like_icon");
        let like_count = target.find(".like_count");

        // Send an AJAX request to like a twit
        $.ajax({
            url: twit_like_url,
            data: {
                twit_id: twit_id,
                twit_action: twit_action
            },
        }).done(function(data) {
            if (data.success) {
                // Update the like button and count based on if the user liked or unliked the twit
                if (twit_action === "like") {
                    target.removeClass("btn-outline-primary");
                    target.addClass("btn-primary");
                    like_icon.removeClass("bi-hand-thumbs-up");
                    like_icon.addClass("bi-hand-thumbs-up-fill");
                    like_count.html(Number(like_count.html()) + 1);
                    target.data("action", "unlike");
                } else {
                    target.removeClass("btn-primary");
                    target.addClass("btn-outline-primary");
                    like_icon.removeClass("bi-hand-thumbs-up-fill");
                    like_icon.addClass("bi-hand-thumbs-up");
                    like_count.html(Number(like_count.html()) - 1);
                    target.data("action", "like");
                }
            }
        });
    });
});