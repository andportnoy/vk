## To-dos

- switch data retrieval functions to parallel execution
- add local storage of data, so that retrieval functions stream to a file as
  opposed to loading everything into memory. for json data it is reasonable
  (and fast) to use ``json.dumps``

## Notes

Saw the following traceback while making a long series of requests through
vk.wall.get. As of now, I only guard against ConnectionError, although I've
seen the following errors previously in similar circumstances. Should I guard
selectively, or against all ``requests`` exceptions? 

---------------------------------------------------------------------------
ConnectionResetError                      Traceback (most recent call last)
/home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/packages/urllib3/response.py
in _error_catcher(self)
    225             try:
    --> 226                 yield
        227 

        /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/packages/urllib3/response.py
        in read(self, amt, decode_content, cache_content)
            300                 cache_content = False
            --> 301                 data = self._fp.read(amt)
                302                 if amt != 0 and not data:  #
                Platform-specific: Buggy versions of Python.

                /home/ec2-user/miniconda3/lib/python3.5/http/client.py in
                read(self, amt)
                    432             b = bytearray(amt)
                    --> 433             n = self.readinto(b)
                        434             return memoryview(b)[:n].tobytes()

                        /home/ec2-user/miniconda3/lib/python3.5/http/client.py
                        in readinto(self, b)
                            472         # (for example, reading in 1k chunks)
                            --> 473         n = self.fp.readinto(b)
                                474         if not n and b:

                                /home/ec2-user/miniconda3/lib/python3.5/socket.py
                                in readinto(self, b)
                                    574             try:
                                    --> 575                 return
                                    self._sock.recv_into(b)
                                        576             except timeout:

                                        /home/ec2-user/miniconda3/lib/python3.5/ssl.py
                                        in recv_into(self, buffer, nbytes,
                                        flags)
                                            923
                                            self.__class__)
                                            --> 924             return
                                            self.read(nbytes, buffer)
                                                925         else:

                                                /home/ec2-user/miniconda3/lib/python3.5/ssl.py
                                                in read(self, len, buffer)
                                                    785         try:
                                                    --> 786             return
                                                    self._sslobj.read(len,
                                                    buffer)
                                                        787         except
                                                        SSLError as x:

                                                        /home/ec2-user/miniconda3/lib/python3.5/ssl.py
                                                        in read(self, len,
                                                        buffer)
                                                            569         if
                                                            buffer is not None:
                                                            --> 570
                                                            v =
                                                            self._sslobj.read(len,
                                                            buffer)
                                                                571
                                                                else:

                                                                ConnectionResetError:
                                                                [Errno 104]
                                                                Connection
                                                                reset by peer

                                                                During handling
                                                                of the above
                                                                exception,
                                                                another
                                                                exception
                                                                occurred:

                                                                ProtocolError
                                                                Traceback (most
                                                                recent call
                                                                last)
                                                                /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/models.py
                                                                in generate()
                                                                    659
                                                                    try:
                                                                    --> 660
                                                                    for chunk
                                                                    in
                                                                    self.raw.stream(chunk_size,
                                                                    decode_content=True):
                                                                        661
                                                                        yield
                                                                        chunk

                                                                        /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/packages/urllib3/response.py
                                                                        in
                                                                        stream(self,
                                                                        amt,
                                                                        decode_content)
                                                                            343
                                                                            while
                                                                            not
                                                                            is_fp_closed(self._fp):
                                                                            -->
                                                                            344
                                                                            data
                                                                            =
                                                                            self.read(amt=amt,
                                                                            decode_content=decode_content)
                                                                                345 

                                                                                /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/packages/urllib3/response.py
                                                                                in
                                                                                read(self,
                                                                                amt,
                                                                                decode_content,
                                                                                cache_content)
                                                                                    310
                                                                                    self._fp.close()
                                                                                    -->
                                                                                    311
                                                                                    flush_decoder
                                                                                    =
                                                                                    True
                                                                                        312 

                                                                                        /home/ec2-user/miniconda3/lib/python3.5/contextlib.py
                                                                                        in
                                                                                        __exit__(self,
                                                                                        type,
                                                                                        value,
                                                                                        traceback)
                                                                                             76
                                                                                             try:
                                                                                             --->
                                                                                             77
                                                                                             self.gen.throw(type,
                                                                                             value,
                                                                                             traceback)
                                                                                                  78
                                                                                                  raise
                                                                                                  RuntimeError("generator
                                                                                                  didn't
                                                                                                  stop
                                                                                                  after
                                                                                                  throw()")

                                                                                                  /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/packages/urllib3/response.py
                                                                                                  in
                                                                                                  _error_catcher(self)
                                                                                                      243
                                                                                                      # This
                                                                                                      # includes
                                                                                                      # IncompleteRead.
                                                                                                      -->
                                                                                                      244
                                                                                                      raise
                                                                                                      ProtocolError('Connection
                                                                                                      broken:
                                                                                                      %r'
                                                                                                      %%
                                                                                                      %e,
                                                                                                      %e)
                                                                                                          245 

                                                                                                          ProtocolError:
                                                                                                          ("Connection
                                                                                                          broken:
                                                                                                          ConnectionResetError(104,
                                                                                                          'Connection
                                                                                                          reset
                                                                                                          by
                                                                                                          peer')",
                                                                                                          ConnectionResetError(104,
                                                                                                          'Connection
                                                                                                          reset
                                                                                                          by
                                                                                                          peer'))

                                                                                                          During
                                                                                                          handling
                                                                                                          of
                                                                                                          the
                                                                                                          above
                                                                                                          exception,
                                                                                                          another
                                                                                                          exception
                                                                                                          occurred:

                                                                                                          ChunkedEncodingError
                                                                                                          Traceback
                                                                                                          (most
                                                                                                          recent
                                                                                                          call
                                                                                                          last)
                                                                                                          <ipython-input-2-eedacc8d555b>
                                                                                                          in
                                                                                                          <module>()
                                                                                                                6 
                                                                                                                      7
                                                                                                                      for
                                                                                                                      friend
                                                                                                                      in
                                                                                                                      tqdm(friends,
                                                                                                                      desc='Friends'):
                                                                                                                      ---->
                                                                                                                      8
                                                                                                                      posts
                                                                                                                      =
                                                                                                                      vk.wall.get(access_token=token,
                                                                                                                      owner_id=friend)
                                                                                                                            9
                                                                                                                            usage
                                                                                                                            =
                                                                                                                            {**usage,
                                                                                                                            **{friend:
                                                                                                                            Counter(item['post_source']['type']
                                                                                                                            for
                                                                                                                            item
                                                                                                                            in
                                                                                                                            posts)}}
                                                                                                                                 10 

                                                                                                                                 /home/ec2-user/vk/wall.py
                                                                                                                                 in
                                                                                                                                 get(access_token,
                                                                                                                                 owner_id,
                                                                                                                                 domain,
                                                                                                                                 filter,
                                                                                                                                 extended,
                                                                                                                                 fields)
                                                                                                                                      16
                                                                                                                                      for
                                                                                                                                      i
                                                                                                                                      in
                                                                                                                                      tqdm(range(n_batches),
                                                                                                                                      desc=str(owner_id)):
                                                                                                                                           17
                                                                                                                                           offset
                                                                                                                                           =
                                                                                                                                           batch_size
                                                                                                                                           * i
                                                                                                                                           --->
                                                                                                                                           18
                                                                                                                                           posts
                                                                                                                                           +=
                                                                                                                                           _get_batch_of_posts(**params_dict,
                                                                                                                                           offset=offset)['items']
                                                                                                                                                19 
                                                                                                                                                     20
                                                                                                                                                     return
                                                                                                                                                     posts

                                                                                                                                                     /home/ec2-user/vk/wall.py
                                                                                                                                                     in
                                                                                                                                                     _get_batch_of_posts(access_token,
                                                                                                                                                     owner_id,
                                                                                                                                                     domain,
                                                                                                                                                     offset,
                                                                                                                                                     count,
                                                                                                                                                     filter,
                                                                                                                                                     extended,
                                                                                                                                                     fields)
                                                                                                                                                          29 
                                                                                                                                                               30
                                                                                                                                                               params_dict
                                                                                                                                                               =
                                                                                                                                                               core.params_dict_from_locals(locals())
                                                                                                                                                               --->
                                                                                                                                                               31
                                                                                                                                                               result
                                                                                                                                                               =
                                                                                                                                                               core.vdr('wall.get',
                                                                                                                                                               params_dict=params_dict)
                                                                                                                                                                    32 
                                                                                                                                                                         33
                                                                                                                                                                         return
                                                                                                                                                                         result

                                                                                                                                                                         /home/ec2-user/vk/core.py
                                                                                                                                                                         in
                                                                                                                                                                         vdr(method,
                                                                                                                                                                         params_dict)
                                                                                                                                                                              67
                                                                                                                                                                              while
                                                                                                                                                                              True:
                                                                                                                                                                                   68
                                                                                                                                                                                   try:
                                                                                                                                                                                   --->
                                                                                                                                                                                   69
                                                                                                                                                                                   raw_response
                                                                                                                                                                                   =
                                                                                                                                                                                   requests.post(api_url,
                                                                                                                                                                                   data=params_dict)
                                                                                                                                                                                        70
                                                                                                                                                                                        except
                                                                                                                                                                                        ConnectionError:
                                                                                                                                                                                             71
                                                                                                                                                                                             print('Connection
                                                                                                                                                                                             error.
                                                                                                                                                                                             Retrying
                                                                                                                                                                                             in
                                                                                                                                                                                             1
                                                                                                                                                                                             s.')

                                                                                                                                                                                             /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/api.py
                                                                                                                                                                                             in
                                                                                                                                                                                             post(url,
                                                                                                                                                                                             data,
                                                                                                                                                                                             json,
                                                                                                                                                                                             **kwargs)
                                                                                                                                                                                                 105
                                                                                                                                                                                                 """
                                                                                                                                                                                                     106 
                                                                                                                                                                                                     -->
                                                                                                                                                                                                     107
                                                                                                                                                                                                     return
                                                                                                                                                                                                     request('post',
                                                                                                                                                                                                     url,
                                                                                                                                                                                                     data=data,
                                                                                                                                                                                                     json=json,
                                                                                                                                                                                                     **kwargs)
                                                                                                                                                                                                         108 
                                                                                                                                                                                                             109 

                                                                                                                                                                                                             /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/api.py
                                                                                                                                                                                                             in
                                                                                                                                                                                                             request(method,
                                                                                                                                                                                                             url,
                                                                                                                                                                                                             **kwargs)
                                                                                                                                                                                                                  51
                                                                                                                                                                                                                  # cases,
                                                                                                                                                                                                                  # and
                                                                                                                                                                                                                  # look
                                                                                                                                                                                                                  # like
                                                                                                                                                                                                                  # a
                                                                                                                                                                                                                  # memory
                                                                                                                                                                                                                  # leak
                                                                                                                                                                                                                  # in
                                                                                                                                                                                                                  # others.
                                                                                                                                                                                                                       52
                                                                                                                                                                                                                       with
                                                                                                                                                                                                                       sessions.Session()
                                                                                                                                                                                                                       as
                                                                                                                                                                                                                       session:
                                                                                                                                                                                                                       --->
                                                                                                                                                                                                                       53
                                                                                                                                                                                                                       return
                                                                                                                                                                                                                       session.request(method=method,
                                                                                                                                                                                                                       url=url,
                                                                                                                                                                                                                       **kwargs)
                                                                                                                                                                                                                            54 
                                                                                                                                                                                                                                 55 

                                                                                                                                                                                                                                 /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/sessions.py
                                                                                                                                                                                                                                 in
                                                                                                                                                                                                                                 request(self,
                                                                                                                                                                                                                                 method,
                                                                                                                                                                                                                                 url,
                                                                                                                                                                                                                                 params,
                                                                                                                                                                                                                                 data,
                                                                                                                                                                                                                                 headers,
                                                                                                                                                                                                                                 cookies,
                                                                                                                                                                                                                                 files,
                                                                                                                                                                                                                                 auth,
                                                                                                                                                                                                                                 timeout,
                                                                                                                                                                                                                                 allow_redirects,
                                                                                                                                                                                                                                 proxies,
                                                                                                                                                                                                                                 hooks,
                                                                                                                                                                                                                                 stream,
                                                                                                                                                                                                                                 verify,
                                                                                                                                                                                                                                 cert,
                                                                                                                                                                                                                                 json)
                                                                                                                                                                                                                                     466
                                                                                                                                                                                                                                     }
                                                                                                                                                                                                                                         467
                                                                                                                                                                                                                                         send_kwargs.update(settings)
                                                                                                                                                                                                                                         -->
                                                                                                                                                                                                                                         468
                                                                                                                                                                                                                                         resp
                                                                                                                                                                                                                                         =
                                                                                                                                                                                                                                         self.send(prep,
                                                                                                                                                                                                                                         **send_kwargs)
                                                                                                                                                                                                                                             469 
                                                                                                                                                                                                                                                 470
                                                                                                                                                                                                                                                 return
                                                                                                                                                                                                                                                 resp

                                                                                                                                                                                                                                                 /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/sessions.py
                                                                                                                                                                                                                                                 in
                                                                                                                                                                                                                                                 send(self,
                                                                                                                                                                                                                                                 request,
                                                                                                                                                                                                                                                 **kwargs)
                                                                                                                                                                                                                                                     606 
                                                                                                                                                                                                                                                         607
                                                                                                                                                                                                                                                         if
                                                                                                                                                                                                                                                         not
                                                                                                                                                                                                                                                         stream:
                                                                                                                                                                                                                                                         -->
                                                                                                                                                                                                                                                         608
                                                                                                                                                                                                                                                         r.content
                                                                                                                                                                                                                                                             609 
                                                                                                                                                                                                                                                                 610
                                                                                                                                                                                                                                                                 return
                                                                                                                                                                                                                                                                 r

                                                                                                                                                                                                                                                                 /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/models.py
                                                                                                                                                                                                                                                                 in
                                                                                                                                                                                                                                                                 content(self)
                                                                                                                                                                                                                                                                     735
                                                                                                                                                                                                                                                                     self._content
                                                                                                                                                                                                                                                                     =
                                                                                                                                                                                                                                                                     None
                                                                                                                                                                                                                                                                         736
                                                                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                                                         -->
                                                                                                                                                                                                                                                                         737
                                                                                                                                                                                                                                                                         self._content
                                                                                                                                                                                                                                                                         =
                                                                                                                                                                                                                                                                         bytes().join(self.iter_content(CONTENT_CHUNK_SIZE))
                                                                                                                                                                                                                                                                         or
                                                                                                                                                                                                                                                                         bytes()
                                                                                                                                                                                                                                                                             738 
                                                                                                                                                                                                                                                                                 739
                                                                                                                                                                                                                                                                                 except
                                                                                                                                                                                                                                                                                 AttributeError:

                                                                                                                                                                                                                                                                                 /home/ec2-user/miniconda3/lib/python3.5/site-packages/requests/models.py
                                                                                                                                                                                                                                                                                 in
                                                                                                                                                                                                                                                                                 generate()
                                                                                                                                                                                                                                                                                     661
                                                                                                                                                                                                                                                                                     yield
                                                                                                                                                                                                                                                                                     chunk
                                                                                                                                                                                                                                                                                         662
                                                                                                                                                                                                                                                                                         except
                                                                                                                                                                                                                                                                                         ProtocolError
                                                                                                                                                                                                                                                                                         as
                                                                                                                                                                                                                                                                                         e:
                                                                                                                                                                                                                                                                                         -->
                                                                                                                                                                                                                                                                                         663
                                                                                                                                                                                                                                                                                         raise
                                                                                                                                                                                                                                                                                         ChunkedEncodingError(e)
                                                                                                                                                                                                                                                                                             664
                                                                                                                                                                                                                                                                                             except
                                                                                                                                                                                                                                                                                             DecodeError
                                                                                                                                                                                                                                                                                             as
                                                                                                                                                                                                                                                                                             e:
                                                                                                                                                                                                                                                                                                 665
                                                                                                                                                                                                                                                                                                 raise
                                                                                                                                                                                                                                                                                                 ContentDecodingError(e)

                                                                                                                                                                                                                                                                                                 ChunkedEncodingError:
                                                                                                                                                                                                                                                                                                 ("Connection
                                                                                                                                                                                                                                                                                                 broken:
                                                                                                                                                                                                                                                                                                 ConnectionResetError(104,
                                                                                                                                                                                                                                                                                                 'Connection
                                                                                                                                                                                                                                                                                                 reset
                                                                                                                                                                                                                                                                                                 by
                                                                                                                                                                                                                                                                                                 peer')",
                                                                                                                                                                                                                                                                                                 ConnectionResetError(104,
                                                                                                                                                                                                                                                                                                 'Connection
                                                                                                                                                                                                                                                                                                 reset
                                                                                                                                                                                                                                                                                                 by
                                                                                                                                                                                                                                                                                                 peer'))
