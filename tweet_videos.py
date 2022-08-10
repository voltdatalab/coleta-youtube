if __name__ == '__main__':
    from database import get_video_to_tweet
    from database import update_video
    from database import mark_published
    import pafy
    import twitter

    video, captions, numbers = get_video_to_tweet()
    #atualiza informações do vídeo
    if video:
        try:
            source = pafy.new(video.yt_video_id, gdata=True)
            update_video(source)
        except:
            print("removido: " + video.yt_video_id)
            print()

        print("```")
        string = "🔍Encontramos {:,} termos que geralmente são usados em contexto de desinformação no vídeo:\n\n\"{}\", do canal: \"{}\".👇".format(len(numbers), video.title, video.author)
        last_status = twitter.simple_tweet(string, None)
        print(string)
        print("```")

        print("```")
        
        string = "Os termos com potencial desinformação que encontramos no vídeo foram: \n"
        resto = False
        for key,value in numbers:
            if (len(string + key + ": " + str(value) + " vezes \n")) < 275:
                string = string + key + ": " + str(value) + " vezes \n"
            else:
                last_status = twitter.simple_tweet(string, last_status)
                print(string)
                string = key + "\: " + str(value) + " vezes \n"
                print("```")
                print("```")

        last_status = twitter.simple_tweet(string, last_status)
        print(string)
        print("```")

        print("```")
        string = "Nos ajude a checar se esses termos foram usados para desinformar! Até o momento, o conteúdo tem {:,} visualizações.\n\n🧵No fio, compartilhamos os links para o momento exato em que esses termos são ditos no vídeo.".format(video.viewCount)
        last_status = twitter.simple_tweet(string, last_status)
        print(string)
        print("```")

        old_string = ""
        for caption in captions:
            print("```")
            if (len(caption.terms.split(',')) > 1):
                string = "Os termos \"" + caption.terms + "\" foram mencionado no vídeo em: {:02}h{:02}m".format(int(caption.minute/60), caption.minute%60)
            else:
                string = "O termo \"" + caption.terms + "\" foi mencionado no vídeo em: {:02}h{:02}m".format(int(caption.minute/60), caption.minute%60)
            string = string + "\n\n"
            string = string + "https://www.youtube.com/watch?v=" + video.yt_video_id + "&t=" + str(caption.minute * 60)
            if string != old_string:
                last_status = twitter.simple_tweet(string, last_status)
                old_string = string
                print(string)
                print("```")
    
        mark_published(video)
